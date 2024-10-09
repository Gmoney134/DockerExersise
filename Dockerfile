FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3-pip
RUN pip install Django
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y tzdata
RUN pip install lxml
RUN pip install django spyne
RUN pip install djangorestframework
RUN pip install graphene-django
RUN pip install djangorestframework
RUN pip install djangorestframework-simplejwt
RUN pip install django-graphql-jwt

WORKDIR /webservices/webservices
