import re

def extract_ips(filename):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    with open(filename, 'r') as file:
        content = file.read()
        ips = re.findall(ip_pattern, content)
    
    unique_ips = list(set(ips))
    print("=== Found IP Addresses ===")
    for ip in unique_ips:
        print(ip)
    
    print(f"\nTotal unique IPs: {len(unique_ips)}")
    
    with open('found_ips.txt', 'w') as f:
        for ip in unique_ips:
            f.write(ip + '\n')
    print("Saved to found_ips.txt")

if __name__ == "__main__":
    extract_ips('test.log')
