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
mail.login('rhythmbhiwani@gmail.com', "AcerLaptop787898")
mail.sendmail(sender, reciver, message.as_string())
mail.quit()
