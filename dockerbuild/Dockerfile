FROM  ubuntu:16.04

MAINTAINER silbertmonaphia@gmail.com

RUN  rm /etc/apt/sources.list
COPY sources.list  /etc/apt/
                                                #basic tools
RUN apt-get -y update && apt-get install -y     apt-utils\
                                                vim \
                                                git  \
                                                wget  \
                                                curl  \
                                                tar  \
                                                unzip \

                                                #python3 env
                                                python3\
                                                python3-pip


#clean pkgs 
RUN  apt-get autoclean \
     && apt-get autoremove \
     && apt-get clean \
     && rm -rf /var/lib/apt/lists/*  /tmp/*  /var/tmp/*


#Create 'spiders' Account
RUN useradd -m web
USER web
WORKDIR /home/web
RUN mkdir .pip
USER root
COPY pip.conf /home/web/.pip/
