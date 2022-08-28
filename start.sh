#!/bin/bash
docker build . -t docker-django-api
docker run -p 8000:8000 docker-django-api
