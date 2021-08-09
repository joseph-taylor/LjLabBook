import numpy as np
import tensorflow as tf
from tensorflow import keras

# run with $ python train_cifar10_gan.py

##########################
##########################
##########################
###### USER OPTIONS ######

output_model_path = 'cifar10_generator'
n_epochs = 10

##########################
##########################
##########################
##########################

batch_size = 32
codings_size = 100

(X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()
X_train = np.float32(X_train / 255.0)
X_train = X_train.reshape(-1, 32, 32, 3) * 2.0 - 1.0
dataset = tf.data.Dataset.from_tensor_slices(X_train).shuffle(1000).batch(batch_size, drop_remainder=True).prefetch(1)
n_batches = np.uint(len(X_train) / batch_size)

generator = keras.models.Sequential([
    keras.layers.Dense(8 * 8 * 128, input_shape=[codings_size]),
    keras.layers.Reshape([8, 8, 128]),
    keras.layers.BatchNormalization(),
    keras.layers.Conv2DTranspose(64, kernel_size=5, strides=2, padding='same', activation='selu'),
    keras.layers.BatchNormalization(),
    keras.layers.Conv2DTranspose(3, kernel_size=5, strides=2, padding='same', activation='tanh'),
])

discriminator = keras.models.Sequential([
    keras.layers.Conv2D(64, kernel_size=5, strides=2, padding='same', activation=keras.layers.LeakyReLU(0.2), input_shape=[32, 32, 3]),
    keras.layers.Dropout(0.4),
    keras.layers.Conv2D(128, kernel_size=5, strides=2, padding='same', activation=keras.layers.LeakyReLU(0.2)),
    keras.layers.Dropout(0.4),
    keras.layers.Flatten(),
    keras.layers.Dense(1, activation='sigmoid')
])

gan = keras.models.Sequential([generator, discriminator])

# the trainable attribute is taken into account by Keras only when compiling a model.
# so the discriminator model IS trainable when we call the discriminator's train_on_batch() method
# but the discriminator model IS NOT trainable when we call the gan's train_on_batch() method
discriminator.compile(loss='binary_crossentropy', optimizer='rmsprop')
discriminator.trainable = False
gan.compile(loss='binary_crossentropy', optimizer='rmsprop')

def train_gan(gan, dataset, output_model_path, batch_size, codings_size, n_epochs, n_batches):
    generator, discriminator = gan.layers
    for epoch in range(n_epochs):
        batch_counter = 0
        for X_batch in dataset:
            batch_counter += 1
            print('Epoch Number:', epoch+1, 'of', n_epochs, ' Batch:', batch_counter, 'of', n_batches, '          ', end='\r')

            # phase 1 - training the discriminator
            noise = tf.random.normal(shape=[batch_size, codings_size])
            generated_images = generator(noise)
            X_fake_and_real = tf.concat([generated_images, X_batch], axis=0)
            y1 = tf.constant([[0.0]] * batch_size + [[1.0]] * batch_size)
            discriminator.trainable = True # this is only to get rid of a Keras warning
            discriminator.train_on_batch(X_fake_and_real, y1)

            # phase 2 - training the generator (we want the discriminator model to believe that the fake images are real)
            noise = tf.random.normal(shape=[batch_size, codings_size])
            y2 = tf.constant([[1.0]] * batch_size)
            discriminator.trainable = False # this is only to get rid of a Keras warning
            gan.train_on_batch(noise, y2)

        # save generator model at end of each epoch
        output_model_path_save = output_model_path + '_epoch' + str(epoch+1)
        generator.save(output_model_path_save)

train_gan(gan, dataset, output_model_path, batch_size, codings_size, n_epochs, n_batches)