import subprocess
import re
from collections import defaultdict

# Fetch SSH authentication logs using journalctl
process = subprocess.Popen(['journalctl', '-u', 'ssh', '--no-pager'], stdout=subprocess.PIPE, text=True)
output = process.communicate()[0]
ip_counts = defaultdict(int)

# parse each log line  to detect failed password attempts
for line in output.splitlines():
    if 'Failed password' in line:
        match = re.search(r'from (\S+)', line)
        if match:
            ip = match.group(1)
            ip_counts[ip] += 1

# Generate report and block IPs with 3+ failed attempts
print("=== SSH BRUTE FORCE REPORT ===")
for ip, count in ip_counts.items():
    status = "BLOCKED" if count >= 3 else "MONITORING"
    print(f"IP: {ip} | Attempts: {count} | Status: {status}")
    if count >= 3:
        subprocess.run(['sudo', 'ufw', 'deny', 'from', ip])
        print(f"Action: Blocked {ip} using UFW firewall")
