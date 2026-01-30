#!/usr/bin/env python3

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime
import os

# GraphQL endpoint
transport = RequestsHTTPTransport(
    url="http://localhost:8000/graphql",
    verify=True,
    retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=False)

query = gql("""
query {
  orders(lastDays: 7) {
    id
    customer {
      email
    }
  }
}
""")

response = client.execute(query)

log_file = "/tmp/order_reminders_log.txt"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(log_file, "a") as f:
    for order in response.get("orders", []):
        f.write(f"[{timestamp}] Order ID: {order['id']}, Customer Email: {order['customer']['email']}\n")

print("Order reminders processed!")
