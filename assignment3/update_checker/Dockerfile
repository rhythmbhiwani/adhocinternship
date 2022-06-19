FROM ubuntu
MAINTAINER rhythmbhiwani@gmail.com
RUN apt-get update
RUN apt-get install docker.io -y
RUN mkdir /myscript
COPY checkupdate.sh /myscript/checkupdate.sh
RUN chmod +x /myscript/checkupdate.sh
ENTRYPOINT ["/bin/bash","/myscript/checkupdate.sh"]