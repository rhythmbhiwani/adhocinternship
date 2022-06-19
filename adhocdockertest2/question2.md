# Question 2
#### Run the Command to create the Dockerfile
```
docker build -t adhoc:rhythmbhiwani https://github.com/redashu/summer2020dockertest.git
```

#### Use this command to tag the image
```
docker tag adhoc:rhythmbhiwani rhythmbhiwani/adhoc:rhythmbhiwani
```

#### Then use this to login to docker
```
docker login
```
##### Enter you username and password

#### Run the command to push to docker hub
```
docker push rhythmbhiwani/adhoc:rhythmbhiwani
```


#### The image *rhythmbhiwani/adhoc:rhythmbhiwani* has be uploaded to Docker Hub
##### [Link to the Image](https://hub.docker.com/repository/docker/rhythmbhiwani/adhoc)
