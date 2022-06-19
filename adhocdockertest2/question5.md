# Question 5

#### Creating Docker Volume
```
docker volume create rhythmbhiwaniq5
```

#### Creating Container
```
docker run -it --name rhythmc5q5 -v rhythmbhiwaniq5:/adhocvol -v /etc/passwd:/user.txt alpine sh
```

#### Then inside the container run
```
wc -l user.txt > /adhocvol/usercount.txt
```

#### Lines Count: 28
