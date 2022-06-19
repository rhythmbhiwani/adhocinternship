FROM centos
MAINTAINER rhythmbhiwani@gmail.com
RUN yum install httpd -y
COPY website /var/www/html/
EXPOSE 80
RUN useradd -ms /bin/bash rhythm
RUN dnf install -y sudo
RUN echo "rhythm ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/rhythm && chmod 0440 /etc/sudoers.d/rhythm
RUN echo "ServerName localhost" >> /etc/httpd/conf/httpd.conf
USER rhythm
ENTRYPOINT sudo httpd -DFOREGROUND