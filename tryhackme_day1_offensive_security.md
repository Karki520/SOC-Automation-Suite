TryHackMe Day 1 - Offensive Security Intro
Path: Cyber Security 101 | Date: 27-May-2026 | Points: 32 | Streak: 1

Room Objective:
Understand attacker mindset and basic web application attacks using offensive security tools.

Tasks Completed:

Task 1: Think like a Hacker!
What I Did: Learned difference between offensive and defensive security.
Key Concept: Offensive security means finding weaknesses before attackers do.
SOC Relevance: To defend, we must know how attackers think and operate.

Task 2: Starting the Lab 
What I Did: Launched FakeBank application in virtual browser.
Finding: Located bank account number 8881 in the application.
SOC Relevance: Reconnaissance is the first step of any attack. We monitor for unusual account enumeration in logs.

Task 3: Find Hidden Pages
Tool Used: dirb - Web Content Scanner
Command: dirb http://fakebank.thm
Findings: Discovered hidden URLs:
1. http://fakebank.thm/images
2. http://fakebank.thm/transfer - Admin panel
SOC Relevance: Attackers scan for hidden admin pages. We create SIEM rules to detect directory brute-force attacks.

Task 4: Attack the Admin Page
What I Did: Accessed hidden /transfer admin panel.
Action: Deposited $2000 into account 8881 using admin privileges.
Flag/Proof: Got green pop-up confirming successful exploitation.
SOC Relevance: Exposed admin panels lead to data breach. As SOC Analyst, I must ensure admin pages are not publicly accessible and monitor for unauthorized access.

Key Takeaway for SOC Role:
Learned how attackers use tools like dirb to find hidden admin pages and exploit them. In a real SOC, I would detect this activity in web server logs by looking for 404 errors followed by 200 on sensitive paths, then block the attacker IP.
