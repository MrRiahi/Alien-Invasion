From python:3.9

RUN apt-get update

# Change the working directory
WORKDIR /usr/src/app

# Copy over the files
COPY ./src ./src
COPY ./images ./images
COPY ./requirements.txt ./requirements.txt
COPY ./alien_invasion.py ./

# Install packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the main file
CMD ["python", "./alien_invasion.py"]
