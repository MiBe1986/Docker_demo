# Commands
This document contains information on how to build and execute example 3.

## Create the docker network with specific IP range (network name = "ex3_net")
`docker network create --driver bridge --ip-range 192.168.100.0/28 --subnet 192.168.100.0/28  ex2_net`

## check the created network exsists with
`docker network ls`

## build the Docker images

- Server  
`docker build . -f Dockerfile_server -t python_server:0.0.1`

- Client  
`docker build . -f Dockerfile_client -t python_client:0.0.1`

## Start the containers
- Server  
`docker run -it --rm --net ex2_net --ip 192.168.100.2 --name server python_server:0.0.1` 

- Client (get a new console)  
`docker run -it --rm --net ex2_net --name client python_client:0.0.1` 

## Watch the Server and Client output