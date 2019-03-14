### Docker basic commands

---

Pull an image from docker hub

```
docker pull hello-world
```

List all images installed

```
docker images
```

Run docker image as a container

```
docker run hello-world
```

List only running containers

```
docker ps
```

List all containers

```
docker ps -a
```

Remove docker container

```
docker rm `conatainer_id`
```

Remove docker container and associated volume

```
docker rm -v `conatainer_id`
```

Remove docker image

```
docker rmi `image_id`
```

Creating custom volume

```
docker run -p 8080:8000 -v $(pwd):/var/www/ -w '/var/www/' django python manage.py runserver
```

#### Building custom images with Dockerfile

Key Dockerfile instruction  
`FROM, MAINTAINER, RUN, COPY, ENTRYPOINT, WORKDIR, EXPOSE, ENV, VOLUME`

Create a dockerfile an exmple is [here](./Dockerfile)
Then build your image

```
docker build -f Dockerfile -t samkaris/django .
```

Publish image on docker hub

```
docker login  # first login
docker push `image_name` # e.g samkaris/django
```
