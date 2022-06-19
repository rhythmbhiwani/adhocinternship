FROM centos
MAINTAINER rhythmbhiwani@gmail.com
RUN yum update -y
RUN yum install -y libtool-ltdl 
RUN yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y
RUN yum install ansible -y
RUN yum install bash -y
RUN yum clean all
COPY script.sh /tmp/script.sh
ENTRYPOINT chown -R root:users /var/run/docker.sock && tail -f /dev/null