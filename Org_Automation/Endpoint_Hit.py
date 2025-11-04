import json
import requests
from socket import timeout
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def hit_endpoint(url):
    successful_links = []
    
    print(f"\n=== API Test Started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
    print(f"Testing URL: {url}\n")
    
    if url != "null":
        try:
            # Try to connect to the main API
            print("Connecting to API...")
            response = requests.get(url, timeout=30)
            response.raise_for_status()  # This will raise an exception for bad status codes
            
            data = response.json()
            total_entries = len(data) if isinstance(data, list) else data.get("count", 0)
            print(f"Successfully connected! Found {total_entries} entries.\n")
            
            # Process each entry
            print("Testing individual API endpoints:")
            print("-" * 50)
            
            entries = data if isinstance(data, list) else data.get("entries", [])
            for index, entry in enumerate(entries, 1):
                link = entry.get('Link') or entry.get('url', 'No URL found')
                print(f"\nTesting [{index}/{total_entries}]: {link}")
                
                try:
                    response = requests.get(link, timeout=10)
                    status = response.status_code
                    
                    if status == 200:
                        successful_links.append(link)
                        print(f"✓ Success (Status: {status})")
                    else:
                        print(f"✗ Failed (Status: {status})")
                        
                except requests.exceptions.Timeout:
                    print(f"✗ Failed (Timeout after 10 seconds)")
                    logging.error(f"Timeout accessing {link}")
                except requests.exceptions.RequestException as e:
                    print(f"✗ Failed (Error: {str(e)})")
                    logging.error(f"Error accessing {link}: {str(e)}")
            
            # Print summary
            print("\n=== Summary ===")
            print(f"Total endpoints tested: {total_entries}")
            print(f"Successful connections: {len(successful_links)}")
            print(f"Failed connections: {total_entries - len(successful_links)}")
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Error connecting to main API: {str(e)}")
            logging.error(f"Main API connection error: {str(e)}")
    else:
        print("✗ Error: URL cannot be null")

# Test the API
print("Starting API endpoint test...")
hit_endpoint("https://jsonplaceholder.typicode.com/posts")
