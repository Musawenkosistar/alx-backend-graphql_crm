import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

LOG_FILE = "/tmp/crm_heartbeat_log.txt"

def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    
    # Log heartbeat
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} CRM is alive\n")
    
    # Optional: query GraphQL hello field
    try:
        transport = RequestsHTTPTransport(url="http://localhost:8000/graphql", verify=True)
        client = Client(transport=transport, fetch_schema_from_transport=True)
        query = gql("{ hello }")
        response = client.execute(query)
        with open(LOG_FILE, "a") as f:
            f.write(f"{timestamp} GraphQL hello response: {response}\n")
    except Exception as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"{timestamp} GraphQL check failed: {e}\n")
