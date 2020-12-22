#!/bin/bash
app="docker.test"
docker build --tag ${app} .
docker run -d -p 56733:80 --name=${app} -v $PWD:/app ${app}
