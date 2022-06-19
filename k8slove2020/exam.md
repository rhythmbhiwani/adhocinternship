# Docker and K8S Exam

## Task 1
#### create Dockerfile for httpd named "adhochttpd.dockerfile"
```
FROM centos
MAINTAINER rhythmbhiwani@gmail.com
RUN yum install -y httpd
ENV x=app
EXPOSE 80
RUN mkdir /myapps
RUN mkdir /scripts
COPY beginner-html-site-styled /myapps/app1
COPY project-html-website /myapps/app2
COPY start.sh /scripts/start.sh
RUN chmod +x /scripts/start.sh
ENTRYPOINT ["/bin/bash","/scripts/start.sh"]
```

#### Git clone the webapps grom github
```
git clone https://github.com/mdn/beginner-html-site-styled
git clone https://github.com/microsoft/project-html-website
```

#### Make the script "start.sh"
```
#!/bin/bash

if [ "$x" == "app1" ]
then
        cp -rf /myapps/app1/* /var/www/html/
        httpd -DFOREGROUND

elif [ "$x" == "app2" ]
then
        cp -rf /myapps/app1/* /var/www/html/
        httpd -DFOREGROUND
else
        echo "You have not selected correct env for app1 or app2" > /var/www/html/index.html
        httpd -DFOREGROUND
fi
```
#### Docker build command
```
docker build -f adhochttpd.dockerfile -t rhythmbhiwani/may2020q1:v1 .
```

#### Push to docker hub
```
docker login
docker push rhythmbhiwani/may2020q1:v1
docker logout
```


## Task 2
#### write a pod file and host it k8s
##### Create pod file named "q2.yaml"
```
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    adhoc: rhythmbhiwaniq2
  name: adhocpod1
spec:
  containers:
  - image: nginx
    name: adhocpod1
    ports:
    - containerPort: 80
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Never
status: {}
```
#### Create the pod
```
kubectl create -f q2.yaml
```

#### Create file for service named "q2srvrhythmbhiwani.yaml"
```
apiVersion: v1
kind: Service
metadata:
  name: q2srvrhythmbhiwani
spec:
  type: NodePort
  selector:
    adhoc: rhythmbhiwaniq2
  ports:
    - port: 80
      targetPort: 80
```
#### Create the service
```
kubectl create -f q2svcrhythmbhiwani.yaml
```


## Task 3
#### write podfile with custom scheduling
#### Create a pod file named "q3.yaml"
```
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    adhoc: rhythmbhiwaniq3
  name: adhocpod2
spec:
  nodeSelector:
    kubernetes.io/hostname: ip-172-31-41-104.ec2.internal
  containers:
  - env:
    - name: x
      value: app2
    image: rhythmbhiwani/may2020q1:v1
    name: adhocpod2
    ports:
    - containerPort: 80
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Never
status: {}
```
#### Create the pod
```
kubectl create -f q3.yaml
```

#### Create service file named "q3svcrhythmbhiwani.yaml"
```
apiVersion: v1
kind: Service
metadata:
  name: q3svcrhythmbhiwani
spec:
  type: NodePort
  selector:
    adhoc: rhythmbhiwaniq3
  ports:
    - port: 80
      targetPort: 80
      nodePort: 32123
```
#### Create the service
```
kubectl create -f q3svcrhythmbhiwani.yaml
```


## Task 4
#### create a replicasets
##### Create file named "q4rs.yaml"
```
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: adhocrsrhythmbhiwani4
  labels:
    app: adhocrsrhythmbhiwani4
spec:
  replicas: 1
  selector:
    matchLabels:
      adhoc: rhythmbhiwaniq4 
  template:
    metadata:
      name: adhocpod4
      labels:
        adhoc: rhythmbhiwaniq4
    spec:
      containers:
      - env:
        - name: x
          value: app2
        image: rhythmbhiwani/may2020q1:v1
        imagePullPolicy: Always
        name: adhocpod4
        ports:
        - containerPort: 80
```
#### Create the replicaset from the file
```
kubectl create -f q4rs.yaml
```
#### Create file for service named "q4svcrhythmbhiwani.yaml"
```
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: null
  labels:
    app: adhocrsrhythmbhiwani4
  name: q4svcrhythmbhiwani
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    adhoc: rhythmbhiwaniq4
  type: LoadBalancer
```
#### Create the service
```
kubectl create -f q4svcrhythmbhiwani.yaml
```

## Task 5
#### deployment create
##### Create file named "q1dep1.yaml"
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: adhhocdeprhythmbhiwani5
  labels:
    adhoc: rhythmbhiwaniq5
spec:
  replicas: 3
  selector:
    matchLabels:
      adhoc: rhythmbhiwaniq5
  template:
    metadata:
      labels:
        adhoc: rhythmbhiwaniq5
    spec:
       containers:
        - env:
          - name: x
            value: app2
          image: rhythmbhiwani/may2020q1:v1
          imagePullPolicy: Always
          name: adhocpod2
          ports:
          - containerPort: 80
```
#### Create the deployment
```
kubectl create -f q5dep1.yaml
```
#### Create service file named "q5svcrhythmbhiwani.yaml"
```
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: null
  labels:
    adhoc: q5svcrhythmbhiwani
  name: q5svcrhythmbhiwani
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    adhoc: rhythmbhiwaniq5
  type: LoadBalancer
```
#### Create the service
```
kubectl create -f q5svcrhythmbhiwani.yaml
```


## Task 6
#### configure portainer in k8s
#### Create pod file named "portainer.yaml"
```
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    adhoc: rhythmbhiwaniq6
  name: adhocpod6
spec:
  nodeSelector:
    kubernetes.io/hostname: ip-172-31-41-74.ec2.internal
  containers:
  - image: portainer/portainer
    name: adhocpod6
    ports:
    - containerPort: 9000
```
#### Create the pod
```
kubectl create -f portainer.yaml
```

#### Create service file named "q6svcrhythmbhiwani.yaml"
```
apiVersion: v1
kind: Service
metadata:
  name: q6srvrhythmbhiwani
spec:
  type: NodePort
  selector:
    adhoc: rhythmbhiwaniq6
  ports:
    - port: 9000
      targetPort: 9000
```
#### Create the service
```
kubectl create -f q6svcrhythmbhiwani.yaml
```

## Task 7
#### Run date command every 3 second and store output
#### Create pod file
```
apiVersion: v1
kind: Pod
metadata:
  labels:
    adhoc: rhythmbhiwaniq7
  name: adhocpod7
spec:
  containers:
  - image: alpine
    name: adhocpod7
    command: ["/bin/shsh","-c","while true; do date>>/mnt/date.txt; sleep 3; done"]
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Never
status: {}
```
#### Create pod file
```
kubectl create -f q7.yaml
```


## Task 8
#### Copy the pod data from the link
#### Original Pod File
```
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:   #  is important if you want your application can get the traffic from service 
   x: hello  # label always be in key: value pair and it must be unique 
  name: podexam  # must be unique
spec:
  containers:
  - image: ngix
    name: pod1
    ports:
    - containerPort: 80
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Never
status: {}
```

#### Create the pod
```
kubectl create -f podexam.yml
```

#### Create a nodeport service
```
apiVersion: v1
kind: Service
metadata:
  name: q8srvrhythmbhiwani
spec:
  type: NodePort
  selector:
    x: hello
  ports:
    - port: 80
      targetPort: 80
```
#### Create Service
```
kubectl create -f wow2020rhythmbhiwani.yaml
```

### To correct the pod, update the image name as nginx in the pod file
#### Updated Pod file
```
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:   #  is important if you want your application can get the traffic from service
   x: hello  # label always be in key: value pair and it must be unique
  name: podexam  # must be unique
spec:
  containers:
  - image: nginx
    name: pod1
    ports:
    - containerPort: 80
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Never
status: {}
```

#### To apply the changes without restarting
```
kubectl apply -f podexam.yml
```

## Task 9
#### Jenkins Pod
#### Pod file
```
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    adhoc: rhythmbhiwaniq9
  name: jenkinspod1
spec:
  containers:
  - image: jenkins/jenkins
    name: jenkinspod1
    ports:
    - containerPort: 8080
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}
```
#### Create pod
```
kubectl create -f jenkins.yaml
```
#### Expose the pod
```
kubectl expose pod jenkinspod1 --port 8080 --type NodePort
```
![Jenkins](/jenkins.png)
