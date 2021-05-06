import matplotlib.pyplot as plt
import numpy as np

##########
# DEMO 1 #
##########

x = np.arange(0, 10, 0.2)
y = np.sin(x)

fig1, ax1 = plt.subplots()
ax1.plot(x, 20*y, label="20 * sine")
ax1.plot(x, x, label="linear")
ax1.plot(x, x**2, label="quadratic")

ax1.set_xlabel('x label')
ax1.set_ylabel('y label')
ax1.set_title("Simple Plot")
ax1.set_xlim(0.0, 9.0)
ax1.legend()

fig1.savefig('demo_1.pdf')
plt.close() # to release memory for a figure


##########
# DEMO 2 #
##########

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

fig2, ax2_list = plt.subplots(1, 3, figsize=(9,3))
ax2_list[0].bar(names, values)
ax2_list[1].scatter(names, values)
ax2_list[2].plot(names, values)

fig2.suptitle('Categorical Plotting')

fig2.savefig('demo_2.pdf')
plt.close()


##########
# DEMO 3 #
##########

mu, sigma = 100, 15
z = mu + sigma * np.random.randn(10000)

fig3, ax3 = plt.subplots(1, 1)
n, bins, patches = ax3.hist(z, 50, density=1, facecolor='g', alpha=0.60)

ax3.set_xlabel('Smarts')
ax3.set_ylabel('Probability')
ax3.axis([40, 160, 0, 0.03])
ax3.grid(True)
ax3.text(60, .025, r'$\mu=100, \sigma=15$') # how to do latex text

fig3.savefig('demo_3.pdf')
plt.close()
