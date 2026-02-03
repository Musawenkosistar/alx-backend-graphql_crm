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
        transport = RequestsHTTPTransport(url='http://localhost:8000/graphql', verify=True)
        client = Client(transport=transport, fetch_schema_from_transport=False)

query = gql("""
{
  hello
}
""")

try:
    result = client.execute(query)
except Exception as e:
    print(f"GraphQL endpoint not responding: {e}")
