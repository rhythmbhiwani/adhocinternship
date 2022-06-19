# Question 4
#### Cloning the website repo
```
git clone https://github.com/redashu/beginner-html-site-styled
```

#### Renaming the folder
```
mv beginner-html-site-styled webapp
```

#### Creating Dockerfile
```
FROM centos
MAINTAINER rhythmbhiwani@gmail.com
RUN yum install httpd -y
COPY webapp /var/www/html/
EXPOSE 80
ENTRYPOINT httpd -DFOREGROUND
```

#### Running Container from the Image
```
docker run -d --name rhythmc4q4 -p 8081:80 rhythmbhiwani:q4
```

#### Accessing the website
[Link to Website](http://52.204.127.145:8081/)


#### Tagging the image
```
docker tag rhythmbhiwani:q4 rhythmbhiwani/rhythm:q4
```

#### Pushing to Docker HUB
```
docker push rhythmbhiwani/rhythm:q4
```

#### [Docker HUB Image Link](https://hub.docker.com/repository/docker/rhythmbhiwani/rhythm)
