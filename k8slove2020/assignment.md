# Kubernetes Assignment Solutions
## Task 1
### Pods creation :
* Create 10 pods by name of adhoc1-adhoc10
* Use alpine docker image with ping 8.8.8.8 as default entrypoint command

#### Create python script named "podsmaker.py"
```
import os
for i in range(1,11):
    print("launching .... adhoc{}".format(i))
    os.system("kubectl run adhoc{} --image=alpine --command ping 8.8.8.8".format(i))
```
#### Run the program
```
python podsmaker.py
```
![Podsmaker Output](/podsmaker.png)


## Task 2
### Dynamic web app :
* Create a pod named nginxpod and use nginx docker image
* Use port 80 as container and service port
```
 kubectl run nginxpod --image=nginx --restart Never --port 80
```
* Create a service nodeport type by exposing the pod
```
kubectl expose pod nginxpod --port 80 --type NodePort
```
* Access web page and take screenshot of it
![Nginx Start Page](/startpagenginx.png)
* After accessing the web page you need to write a shell | python | go code in current running
nginxpod
* Script that you write it must connect to kube-apiversion and list all the running pods in k8s
cluster
* Store the output of above command under /usr/share/nginx/html/index.html
#### Create a ClusterRoleBinding to give permission to pod to access the api server named "roles.yaml"
```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: default-view
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: view
subjects:
  - kind: ServiceAccount
    name: default
    namespace: default
```
#### Create it
```
kubectl create -f roles.yaml
```
#### Exec into the pod
```
kubectl exec -it nginxpod bash
```
#### Run These commands
```
apt-get update && apt-get install python3 python3-pip -y
pip3 install kubernetes
```
#### Save this python script named "generatehtml.py"
```
from kubernetes import client, config
config.load_incluster_config()
v1 = client.CoreV1Api()

podsList = v1.list_pod_for_all_namespaces(watch=False)

originalHTML = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <title>List of PODS</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
  <table class="table">
    <thead class="thead-dark">
      <tr>
        <th scope="col">Pod IP</th>
        <th scope="col">Namespace</th>
        <th scope="col">Name</th>
      </tr>
    </thead>
    <tbody>
"""
for i in podsList.items:
    originalHTML+="""
        <tr>
    <th scope="row">{}</th>
    <td>{}</td>
    <td>{}</td>
        </tr>
    """.format(i.status.pod_ip, i.metadata.namespace, i.metadata.name)
originalHTML+="""
</tbody>
</table>
</body>
</html>
"""

with open("/usr/share/nginx/html/index.html",'w') as index:
    index.write(originalHTML)

```
#### Run the script
```
python3 generatehtml.py
```
* Now reload the webpage take screenshot again
![Updated Pods List](/podslist.png)


## Task 3
### Email Pod:
* Very much similar to dynamic web app question but here we don’t need to store the data as
page
* Here we have to send all running pods and services names only to the email address
* Email id is learntechbyme@gmail.com with subject <yournamek8slove2020>
    
#### Enable this for login access by going to 
https://myaccount.google.com/lesssecureapps
#### Write python script "sendmail.py"
```
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from kubernetes import client, config
import os
config.load_incluster_config()
v1 = client.CoreV1Api()
podsList = v1.list_pod_for_all_namespaces(watch=False)

originalHTML = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <title>List of PODS</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
  <table class="table">
    <thead class="thead-dark">
      <tr>
        <th scope="col">Pod IP</th>
        <th scope="col">Namespace</th>
        <th scope="col">Name</th>
      </tr>
    </thead>
    <tbody>
"""
for i in podsList.items:
    originalHTML+="""
        <tr>
    <th scope="row">{}</th>
    <td>{}</td>
    <td>{}</td>
        </tr>
    """.format(i.status.pod_ip, i.metadata.namespace, i.metadata.name)
originalHTML+="""
</tbody>
</table>
</body>
</html>
"""

sender = "rhythmbhiwani@gmail.com"
reciver = "learntechbyme@gmail.com"

message = MIMEMultipart('alternative')
message['Subject'] = "rhythmbhiwanik8slove2020"
message['From'] = sender
message['To'] = reciver
htmlfile = MIMEText(originalHTML, 'html')
message.attach(htmlfile)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('rhythmbhiwani@gmail.com', "PASSWORD HERE")
mail.sendmail(sender, reciver, message.as_string())
mail.quit()
```
#### Run the script
```
python3 sendmail.py
```
