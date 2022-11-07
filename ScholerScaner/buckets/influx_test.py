import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

import logging

logger = logging.getLogger(__name__)

influx_token = os.environ.get("INFLUXDB_TOKEN",
                              'ddMZE4c-MoLJCDQp_p1SJkgHPXqRzFZ25szVXOM0jREsMr12NgeLHhX7IW8A1aedrRSBJR8b1Z-xnIC-vp7N-g=='
                              )
org = "Sindustry"
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(url=url, token=influx_token, org=org)

bucket = "SchoolerBucket"

write_api = client.write_api(write_options=SYNCHRONOUS)

for value in range(5):
    point = (
        Point("measurement1")
        .tag("tagname1", "tagvalue1")
        .field("field1", value)
    )
    write_api.write(bucket=bucket, org="Sindustry", record=point)
    time.sleep(1)  # separate points by 1 second

query_api = client.query_api()

query = """from(bucket: "SchoolerBucket")
 |> range(start: -10m)
 |> filter(fn: (r) => r._measurement == "measurement1")"""
tables = query_api.query(query, org="Sindustry")

for table in tables:
    for record in table.records:
        print(record)

print('---------------------')

query_api = client.query_api()

query = """from(bucket: "SchoolerBucket")
  |> range(start: -10m)
  |> filter(fn: (r) => r._measurement == "measurement1")
  |> mean()"""
tables = query_api.query(query, org="Sindustry")

for table in tables:
    for record in table.records:
        print(record)