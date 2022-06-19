from centos
maintainer rhythmbhiwani@gmail.com
run yum install httpd -y
run mkdir /mycode
env x=webapp1	
#this variable will be availabe in docker image that will be created
copy webapp1 /mycode/webapp1
copy webapp2 /mycode/webapp2
copy startweb.sh /mycode/startweb.sh
run chmod +x /mycode/startweb.sh
expose 80
entrypoint ["/bin/bash","/mycode/startweb.sh"]