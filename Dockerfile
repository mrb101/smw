# Base Image
FROM ubuntu:16.04

# Maintainer of this Image
MAINTAINER Bassel J. hamadeh <hamadeh.bassel@protonmail.ch>

# install essential packages
# clean
RUN apt-get update \
  && apt-get install -y tar curl git vim wget build-essential \
  && apt-get clean

# Update ubuntu's package manager repository
# Install essential packages
# Clean
RUN apt-get install -y python-setuptools python-distribute python-dev build-essential python-psycopg2 \
  && apt-get clean

# download get-pip.py script
# run get-pip.py script to install pip
# remove get-pip.py script
RUN curl -L https://bootstrap.pypa.io/get-pip.py > get-pip.py \
  && python get-pip.py \
  && rm get-pip.py

# install virtualenv python package
RUN pip install virtualenv

# create a virtualenv
RUN cd /srv \
  && virtualenv venv

# activate the virtualenv
RUN /bin/bash -c "cd /srv/ && source venv/bin/activate" \
  && pip install django

# create app dir
RUN mkdir /srv/app 

# Create a temp dir to install requirements
RUN mkdir /srv/temp

# copy the app files to the container
COPY app/requirements.txt /srv/temp

# Install the requirements
RUN pip install -r /srv/temp/requirements.txt

# Share files with the host
# COPY app /srv/app

EXPOSE 4000

# set work directory
WORKDIR /srv/app

# RUN THE SERVER
CMD python manage.py runserver 0.0.0.0:4000
