# Commands
This document contains information on how to build and execute example 1.  
Also check the official *[docker documentation](https://docs.docker.com/engine/reference/commandline/docker/)*

### layer concept
### mounting volumes etc.

## Short list of most used docker commands
- docker build
- docker run
- docker images
- docker ps
- docker inspect
- docker network 
- docker login
- docker pull
- docker push
- docker exec
- docker attach
- docker stop

## Commands for example 1

### build the container
`docker build . -f Dockerfile --build-arg buildarg1="this is arg1" -t example1:0.0.1`

### run the container
`docker run -it --rm --name example1  example1:0.0.1`

### show local docker images
`docker images`

### inspect the image
`docker inspect example:0.0.1`

### remove the image
`docker rmi example:0.0.1`

### tagging/push/pull of images from remote docker registry
* Suppose we have a remote docker registry called "thinktank_acr.azurecr.io"
* login to remote registry with `docker login thinktank_acr.azurecr.io -u <USER> -p <PASSWORD>`
* local image example:0.0.1
* pushing the local image to the remote repository requires tagging  
    `docker tag example:0.0.1 thinktank_acr.azurecr.io/example:0.0.1`
* now you can push the image with `docker push thinktank_acr.azurecr.io/example:0.0.1`