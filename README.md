# SOC Automation Suite

Python-based security automation toolkit for SOC analysts and blue teams. Designed to automate repetitive L1 SOC tasks.

## Tools Included

### 1. SSH Brute Force Detector
Monitors `/var/log/auth.log` to identify SSH brute force attempts in real-time. Flags IPs exceeding 5 failed login attempts and generates alerts for IP blocking.

**Key Features:**
- Log parsing using regex
- Configurable threshold for failed attempts
- Timestamped alert generation

**Use Case:** SOC L1 monitoring, SIEM rule prototyping, incident response triage.

### 2. Port Scanner
Multithreaded TCP connect scanner for fast network reconnaissance. Identifies open ports on target hosts to support asset discovery.

**Key Features:**
- Multithreading for speed
- Scans common ports 1-1024
- Clean CLI output

**Use Case:** Network auditing, vulnerability assessment, pre-engagement recon.

## Tech Stack
- **Language:** Python 3
- **Core Libraries:** socket, threading, re, datetime
- **Platform:** Linux / Kali Linux

## Setup & Usage
```bash
# Clone repo
git clone https://github.com/Karki520/SOC-Automation-Suite

# Run SSH detector
sudo python3 ssh_brute_detector.py

# Run port scanner
python3 port_scanner.py <target_ip>

## Disclaimer
For educational and authorized security testing only. Use only on networks you own or have explicit permission to test.

## Author
pooja karki| Aspiring SOC Analyst | Cybersecurity Enthusiast
