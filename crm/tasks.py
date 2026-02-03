from celery import shared_task
from datetime import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

LOG_FILE = "/tmp/crm_report_log.txt"

@shared_task
def generate_crm_report():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # GraphQL client
    transport = RequestsHTTPTransport(url='http://localhost:8000/graphql', verify=True)
    client = Client(transport=transport, fetch_schema_from_transport=False)

    query = gql("""
    {
        totalCustomers
        totalOrders
        totalRevenue
    }
    """)
    
    try:
        result = client.execute(query)
        report_line = (
            f"{timestamp} - Report: "
            f"{result['totalCustomers']} customers, "
            f"{result['totalOrders']} orders, "
            f"{result['totalRevenue']} revenue\n"
        )
        
        with open(LOG_FILE, "a") as f:
            f.write(report_line)

    except Exception as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"{timestamp} - Error generating report: {e}\n")

