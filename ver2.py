import json
from google.cloud import bigquery
from google.oauth2 import service_account

# Construct a BigQuery client object.
project_id = 'dev-country-196401'
client = bigquery.Client(project=project_id)


# TODO(developer): Set table_id to the ID of the table to create.
table_id = "dev-country-196401.data_models.localidade"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("geolocation_zip_code_prefix", "INTEGER"),
        bigquery.SchemaField("geolocation_lat", "FLOAT"),
        bigquery.SchemaField("geolocation_lng", "FLOAT"),
        bigquery.SchemaField("geolocation_city", "STRING"),
        bigquery.SchemaField("geolocation_state", "STRING"),
     ],
    skip_leading_rows=1,
    source_format= bigquery.SourceFormat.CSV,
)
uri = "gs://danipipe1/data.csv"

load_job = client.load_table_from_uri(
uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Wait for the job to complete.

table = client.get_table(table_id)