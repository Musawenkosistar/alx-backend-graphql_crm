from datetime import datetime 
from gql import gql, Client 
from gql.transport.requests import RequestsHTTPTransport

def log_crm_heartbeat():
    timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

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

        result = client.execute(query)
        print("GraphQL hello response:", result)
    except Exception as e:
        print(f"GraphQL endpoint not responding: {e}")

def update_low_stock():
    timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    log_file = "/tmp/low_stock_updates_log.txt"

    try:
        transport = RequestsHTTPTransport(url='http://localhost:8000/graphql', verify=True)
        client = Client(transport=transport, fetch_schema_from_transport=False)

        mutation = gql("""
        mutation {
            updateLowStockProducts {
                updatedProducts {
                    id
                    name
                    stock
                }
                message
            }
        }
        """)

        result = client.execute(mutation)
        products = result['updateLowStockProducts']['updatedProducts']
        message = result['updateLowStockProducts']['message']

        with open(log_file, "a") as f:
            f.write(f"{timestamp} - {message}\n")
            for p in products:
                f.write(f"{timestamp} - Product: {p['name']}, Stock: {p['stock']}\n")

    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - Error: {e}\n")
