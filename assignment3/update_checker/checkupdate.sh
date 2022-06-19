#!/bin/bash

while :
do
	LATEST=`docker image ls rhythmassignment:v3 --no-trunc --format "{{.ID}}"`
	RUNNING=`docker inspect --format='{{.Image}}' website_container`
	if [ "$RUNNING" != "$LATEST" ]
	then
		`docker rm -f website_container`
		`docker run -d --name website_container -p 80:80 rhythmassignment:v3`
		echo "Container Updated"
	else
        	echo "Website up to date"
	fi
	sleep 1
done