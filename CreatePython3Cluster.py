import requests

response = requests.post(
    'https://westeurope.azuredatabricks.net/api/2.0/clusters/create',
    json={
        'cluster_name': 'ntedemodbrstreamingdemoscript',
        'num_workers': 2,
        'spark_version': '3.2.x-scala2.11',
        'spark_env_vars': {
          'PYSPARK_PYTHON': '/databricks/python3/bin/python3',
         }
    },
    headers={'Authorization' : 'Bearer dapi9cb3739eadea927eb328cfa6a822c913'}
)

if response.status_code == 200:
    print(response.json())
else:
    print("Error launching cluster: %s: %s" % (response.json()["error_code"], response.json()["message"]))
