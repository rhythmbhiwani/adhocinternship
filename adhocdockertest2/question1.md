# Question 1
#### Create Dockerfile as follows
```
FROM alpine
MAINTAINER rhythmbhiwani@gmail.com
ENTRYPOINT date +%T
```

#### Build the image from Dockerfile as follows
```
docker build -t alpine:rhythmbhiwani .
```

#### Create containers
#### Create 1st Container
```
docker run --name rhythmc1q1 alpine:rhythmbhiwani >> question1.txt
```

#### Create 2nd Container
```
docker run --name rhythmc2q1 alpine:rhythmbhiwani >> question1.txt
```

#### Now the 2 time values will be saved in your file named question1.txt
