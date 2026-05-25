# SOC Automation Suite

A collection of Python-based automation tools designed for Security Operations Center (SOC) L1 tasks. This project demonstrates practical application of programming in cybersecurity.

## Why I Built This
I'm an MCA student with  exposure to Java, Python, and Web Development. I built this SOC Automation Suite to explore cybersecurity and apply my Programming fundamentals to real-world security problems. This project bridges my coding knowledge with Blue Team operations.

## Tools Included

### 1. SSH Brute Force Detector
Monitors `/var/log/auth.log` for repeated failed SSH login attempts. Flags potential brute-force attacks and extracts malicious IP addresses using Regex.

**Tech Used:** Python, Regular Expressions

### 2. Multithreaded Port Scanner
Scans a target IP for open TCP ports using multithreading for faster network reconnaissance. Helps in identifying exposed services during asset discovery.

**Tech Used:** Python, Socket Programming, Multithreading

## Getting Started

### Prerequisites
- Python 3.x
- Linux environment for log monitoring (Kali/Ubuntu recommended)

### Installation
```bash
git clone https://github.com/Karki520/SOC-Automation-Suite.git
cd SOC-Automation-Suite
## Disclaimer
These tools are developed for educational purposes and authorized security testing only. The author is not responsible for any misuse or damage caused by these scripts. Always obtain proper authorization before scanning networks or systems you do not own.

## Author
pooja karki  
MCA Graduate | Programming & Cybersecurity Enthusiast  
Open to SDE & SOC Analyst roles
