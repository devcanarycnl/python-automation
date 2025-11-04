import csv
import pandas as pd
try:
    from kubernetes import client, config
    K8S_AVAILABLE = True
except Exception:
    client = None
    config = None
    K8S_AVAILABLE = False

# Function to load Kubernetes configuration (from kubeconfig file or in-cluster)
def load_k8s_config():
    if not K8S_AVAILABLE:
        print("kubernetes package is not installed. To enable cluster access install: pip install kubernetes")
        return False

    try:
        # Try loading the kubeconfig from the default location (e.g., ~/.kube/config)
        config.load_kube_config()
        return True
    except Exception as e:
        print(f"Error loading Kubernetes config: {e}")
        print("If running inside a cluster, consider using config.load_incluster_config().")
        return False

# Function to fetch pod data from Kubernetes cluster
def fetch_pod_data():
    # If kubernetes client is not available, return empty list
    if not K8S_AVAILABLE:
        return []

    # Create the Kubernetes API client for Pod resources
    v1 = client.CoreV1Api()

    try:
        # Fetch pod information across all namespaces
        pod_list = v1.list_pod_for_all_namespaces(watch=False)
    except Exception as e:
        print(f"Error fetching pods from cluster: {e}")
        return []

    # Prepare a list of dictionaries to store pod data
    pod_data = []
    for pod in pod_list.items:
        pod_data.append({
            "namespace": getattr(pod.metadata, 'namespace', None),
            "name": getattr(pod.metadata, 'name', None),
            "status": getattr(pod.status, 'phase', None),
            "created_at": getattr(pod.metadata, 'creation_timestamp', None),
            "node_name": getattr(pod.spec, 'node_name', None),
        })

    return pod_data

# Function to write data to a CSV file
def write_data_to_csv(data, filename):
    # Define column headers
    headers = ["namespace", "name", "status", "created_at", "node_name"]
    
    # Open CSV file in write mode and write the data
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data written to {filename}")

# Function to read data from the CSV file and load it into a Pandas DataFrame
def read_data_from_csv(filename):
    # Use Pandas to read the CSV file into a DataFrame
    df = pd.read_csv(filename)
    return df

# Main function to run the process
def main():
    # Load Kubernetes configuration
    has_config = load_k8s_config()

    # Fetch pod data from Kubernetes (may be empty)
    pod_data = fetch_pod_data() if has_config else []

    # If we couldn't fetch real data, use mock data so the script demonstrates output
    if not pod_data:
        print("No cluster data available; using mock pod data for demo.")
        pod_data = [
            {"namespace": "default", "name": "app-1", "status": "Running", "created_at": "2025-11-04T10:00:00Z", "node_name": "node-1"},
            {"namespace": "kube-system", "name": "coredns-1", "status": "Running", "created_at": "2025-11-03T08:12:00Z", "node_name": "node-2"},
            {"namespace": "default", "name": "job-123", "status": "Completed", "created_at": "2025-11-02T09:00:00Z", "node_name": "node-3"},
        ]

    # Write the pod data to a CSV file
    csv_filename = 'k8s_pod_data.csv'
    write_data_to_csv(pod_data, csv_filename)

    # Read the data back from the CSV file using Pandas
    df = read_data_from_csv(csv_filename)
    
    # Print the DataFrame to see the loaded data
    print("\nData extracted from the CSV file:")
    print(df)

# Run the main function
if __name__ == "__main__":
    main()
