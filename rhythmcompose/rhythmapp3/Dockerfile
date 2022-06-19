FROM centos
MAINTAINER rhythmbhiwani@gmail.com
ENV x=app
RUN dnf install httpd -y
ADD app /var/www/html
EXPOSE 80
ENTRYPOINT httpd -DFOREGROUND