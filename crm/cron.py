import datetime
import requests

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
