---
title: "Docker"
draft: false
toc:
  auto: false
---

# Handy Tricks for Docker

## List all images
```shell
docker image ls
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

## View Running Images
```shell
docker ps
```


## Stop Running Image
First get the container ID using the `ps` command

```shell
docker kill <container ID>
```