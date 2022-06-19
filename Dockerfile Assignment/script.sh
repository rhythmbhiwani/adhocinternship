#!/bin/bash
f = 1
while [ $f -le 10 ]
do
docker container run -d --name alpine$f alpine fb.com
f = `expr $f + 1 '
done