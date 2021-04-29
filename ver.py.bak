from google.cloud import bigquery
from google.oauth2 import service_account

project_id = 'dev-country-196401'
client = bigquery.Client(project=project_id)

QUERY = (
    'select count(*) from `dev-country-196401.data_models.localidade`')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row)
