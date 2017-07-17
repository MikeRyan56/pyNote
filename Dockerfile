#FROM ubuntu:latest
FROM python:3.6 
MAINTAINER Stu Ryan "mikeryan56@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
EXPOSE 8080
RUN pip install -r requirements.txt
# WORKDIR /data
VOLUME /data
ENTRYPOINT ["fabmanager create-admin"]
ENTRYPOINT ["Admin"]
ENTRYPOINT ["Administrator"]
ENTRYPOINT ["Account"]
ENTRYPOINT ["pyNote@DevSetGo.com"]
ENTRYPOINT ["$Password"]
ENTRYPOINT ["$Password"]
ENTRYPOINT ["fabmanager run"]