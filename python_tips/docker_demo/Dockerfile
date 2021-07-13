# build $ docker build --tag python-app .
# run   $ docker run python-app


# tell docker what base image to use for the application
FROM python:3.8-slim-buster

# create a working directory (docker will use this as the default path)
WORKDIR /app

# copy local files into the image (app.py and requirements.txt)
COPY . .

# run pip install command into the image
RUN pip3 install -r requirements.txt

# execute python script
CMD ["python", "app.py"]