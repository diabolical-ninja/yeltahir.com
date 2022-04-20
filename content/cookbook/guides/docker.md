---
title: "Docker"
draft: false
toc:
  auto: false
---

# Handy Tricks for Docker

## Build New Image
Builds based of current directory
```sh
docker build .
```

With a name & tag
```sh
docker build -t <name>:<tag> .

# Eg
docker build -t awesomeimage:1.0 .
```

## List all images
```shell
docker image ls

# OR
docker ima
```


## Delete an image

First retrieve the image ID using the `ls` command. 
```shell
docker image rm <id>
```

If the image is used by multiple containers & you're sure you want to delete it, you can run:
```shell
docker image rm -f <id>
```

To delete all unused & "dangling" images
```sh
#lists all images that are dangling and has no pointer to it
docker images --filter dangling=true 

#Removes all those images.
docker rmi -f `docker images --filter dangling=true -q` 
```

## Run Image 

```sh
docker run <image name>
```

To explore the built environment
```sh
docker run -it <image name> sh
```


## View Running Images
```shell
docker ps
```


## Stop Running Image
First get the container ID using the `ps` command

```shell
docker kill <container ID>
```