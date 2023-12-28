from faker import Faker
import random
import csv

# Initialize Faker
fake = Faker()

# Define categories and their respective issue summaries, steps, and resolutions
categories = {
    "Server Downtime": {
        "summaries": ["Server unexpectedly down", "Frequent server restarts", "Server unresponsive"],
        "steps": [
            "1. Check server status\n2. Review system logs",
            "1. Monitor server performance\n2. Analyze restart patterns",
            "1. Ping server\n2. Attempt remote access"
        ],
        "resolutions": [
            "After investigating, we found that the server was down due to a failed software update. We rolled back the update, restored the server to its previous stable state, and implemented a more robust update testing protocol.",
            "Analysis of the server logs indicated that the frequent restarts were due to memory leaks in a recently deployed application. We patched the application and optimized memory usage, resolving the restart issues.",
            "The server's unresponsiveness was traced to a network configuration error. We reconfigured the network settings, established a stable connection, and ensured remote access was fully functional."
        ]
    },
    "Database Connectivity Issues": {
        "summaries": ["Database refusing connections", "Slow database queries", "Data replication lag"],
        "steps": [
            "1. Test database connection\n2. Examine error logs",
            "1. Run query performance analysis\n2. Identify bottlenecks",
            "1. Check replication status\n2. Compare data across servers"
        ],
        "resolutions": [
            "The issue of the database refusing connections was due to a firewall misconfiguration. We updated the firewall rules to allow legitimate traffic, tested the database connectivity, and confirmed it was accepting connections.",
            "Our investigation into the slow database queries revealed indexing issues. We restructured the database indexes, optimized the query execution plan, and achieved a significant improvement in query response time.",
            "We addressed the data replication lag by tuning the replication parameters, increasing the network throughput, and ensuring synchronous data replication across all servers, thereby maintaining data consistency."
        ]
    },
    "SSL/TLS Certificate Problems": {
        "summaries": ["SSL certificate expired", "SSL handshake failure", "Mixed content warnings"],
        "steps": [
            "1. Verify certificate expiry\n2. Attempt certificate renewal",
            "1. Analyze SSL handshake process\n2. Check server and client SSL configurations",
            "1. Inspect web content sources\n2. Identify non-secure elements"
        ],
        "resolutions": [
            "The expired SSL certificate was promptly renewed through our certificate authority. We installed the new certificate, verified its validity, and ensured all web traffic is now securely encrypted.",
            "An in-depth analysis of the SSL handshake failure pointed to incompatible SSL protocols between the server and clients. We updated the server's SSL configuration to support a broader range of protocols, resolving the handshake issues.",
            "To address the mixed content warnings, we audited the entire website to identify and update all HTTP links to HTTPS, thereby ensuring all content is securely served over SSL, eliminating the warnings."
        ]
    }
}

# Function to generate a coherent record
def generate_record():
    # Choose a random category and its details
    category, details = random.choice(list(categories.items()))
    summary = random.choice(details["summaries"])
    steps = random.choice(details["steps"])
    resolution = random.choice(details["resolutions"])

    return {
        "issue_id": fake.unique.uuid4(),
        "date_and_time": fake.date_time_this_year(),
        "category": category,
        "issue_summary": summary,
        "steps_to_reproduce": steps,
        "resolution": resolution
    }

# Generate 3000 records
records = [generate_record() for _ in range(3000)]

# Write to a CSV file
file_path = '/mnt/data/synthetic_technical_support_data_v2.csv'
with open(file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)

file_path

