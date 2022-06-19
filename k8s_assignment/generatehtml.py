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
