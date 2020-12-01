FROM ubuntu:20.04

ENV DEBIAN_FRONTEND="noninteractive"
ENV envvar1="This is a hardcoded environment variable"

ARG buildarg1=foo
ENV envvar2=${buildarg1}

RUN apt-get update &&\
    apt-get install -y python3

COPY ./simple_print.py ./simple_print.py

EXPOSE 8080

