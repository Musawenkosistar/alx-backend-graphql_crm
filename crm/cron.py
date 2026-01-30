import datetime
import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    log_message = f"{timestamp} CRM is alive\n"

    # Append to the log file
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(log_message)

    # Optional: test GraphQL hello endpoint
    try:
        response = requests.post(
            "http://localhost:8000/graphql",
            json={"query": "{ hello }"},
            timeout=5
        )
        if response.ok:
            f.write(f"{timestamp} GraphQL endpoint responded\n")
    except requests.exceptions.RequestException:
        f.write(f"{timestamp} GraphQL endpoint not reachable\n")

def log_crm_heartbeat():
    import datetime
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"{timestamp} CRM is alive\n")
    
    # Optional: check GraphQL hello field
    transport = RequestsHTTPTransport(url="http://localhost:8000/graphql", verify=False)
    client = Client(transport=transport, fetch_schema_from_transport=True)
    query = gql("{ hello }")
    try:
        result = client.execute(query)
        with open("/tmp/crm_heartbeat_log.txt", "a") as f:
            f.write(f"{timestamp} GraphQL hello: {result['hello']}\n")
    except Exception as e:
        with open("/tmp/crm_heartbeat_log.txt", "a") as f:
            f.write(f"{timestamp} GraphQL query failed: {e}\n")
