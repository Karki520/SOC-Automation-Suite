import socket

# Target configuration for port scanning
target = "scanme.nmap.org"
ports = [21, 22, 80, 443, 8080]

print(f"=== SCANNING {target} ===")

# Execute TCP connect scan for each specified port
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")

    s.close()

print("=== SCAN COMPLETE ===")
