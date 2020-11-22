# Docker Ninja Tricks - Dockerventure Part 3

`TL;DR` Useful docker commands to have in your arsenal

![](images/docker_logo.png)

So far we 've seen the basic functinality of Docker, had a quick look on common commands used in order to manage/view/build/share containers and images. In this post I am going to try to gather some other useful Docker commands that will make our life easier operating dockerized systems.

## Usefull Docker Commands

In the previous 2 parts we 've already seen:

`docker run`
`docker ps` & `docker ps -a`
`docker stop`
`docker start`
`docker logs`
`docker help`
`docker login`
`docker rm`
`docker build`
`docker images`
`docker push`

So I ll move forward to other more sneaky commands. If you want to check how the previous Docker commands can be used in actions check my 2 previous posts [Exploring the Docker world - Dockerventure Part 1]()  & [Taming the Docker beast - Dockerventure Part 2]()

### docker --version

Quite self explanatory, shows you the currently installed version.

### docker rmi

Used to delete docker images, more or less similar to `docker rm` but for images instead of containers

### docker exec

This command is used in order to execute a command on a running container. Most common use case is to access a running container to debug something.
`docker exec -it <cotnainer_id> bash`

### docker inspect

Used to get detailed low level information on Docker objects like containers and images. If you are looking for details like Ip addresses, volumes, stuff around networking, image layers etc this should be your first place to look.

### docker restart

Quite self explanatory, restarts a docker container

### docker system prune

Used for housekeeping and cleaning in order to remove all unused containers, networks and images, combine with `--volumes` to clean volumes too

### docker top

Display the running processes of a container

### docker volume

Manage volumes by combining with the subcommands `create` , `inspect` `ls` `prune`, `rm`

### docker stats

Get a live stream of resource usage of your running containers. Quite useful for debugging purposes shows CPU, Mem, Net I/o, Block I/o , Pids

### docker network

Manage network by combining with the subcommands `create` , `connect`, `disconnect`, `inspect`, `ls`, `prune`, `rm`
