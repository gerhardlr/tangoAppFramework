FROM gerhardlr/tango_python:latest

#install dependencies
USER root

# Update and install pip
RUN apt-get update 
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN pip install --upgrade pip

#Install requirements

#create workdir conating source code
WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt


#ENTRYPOINT ["python"]
#CMD ["app.py"]

