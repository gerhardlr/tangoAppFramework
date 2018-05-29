FROM gerhardlr/tango_gui:latest

#install dependencies
USER root

# Update.
RUN apt-get update 
RUN apt-get install -y python
RUN apt-get install -y python-pip

# Install app dependencies.
RUN pip install --upgrade pip

#Install requirements

WORKDIR /App
ADD requirements.txt /Testing/requirements.txt

RUN pip install -r requirements.txt
