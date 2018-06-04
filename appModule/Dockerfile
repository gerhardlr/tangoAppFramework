FROM gerhardlr/tango_python:latest

#install dependencies
USER root

#create workdir conating source code
RUN mkdir /home/appModule

WORKDIR /home/appModule

ENV HOME /home/appModule

ADD . /home/appModule
RUN pip install -e .

RUN useradd --create-home --home-dir $HOME developer \
    && chown -R developer:developer $HOME

USER developer
