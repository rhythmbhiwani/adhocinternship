FROM centos
MAINTAINER rhythmbhiwani@gmail.com
RUN yum install httpd -y
COPY webapp /var/www/html/
EXPOSE 80
ENTRYPOINT httpd -DFOREGROUND