# ARP Spoofing & MITM Credential Harvesting Lab

A hands-on lab demonstrating how an attacker on the same VPN can intercept unencrypted HTTP traffic, steal credentials, and return a fake success page—all without the victim knowing.

## Tools Used
- Kali Linux (attacker)
- Tailscale (VPN)
- Python (HTTP server + form handler)
- tcpdump (packet sniffing)
- HTML/CSS (phishing page)

## Objective
To simulate a real-world man-in-the-middle attack and capture plaintext credentials over HTTP.

## Lab Setup
- IP
- Both connected via Tailscale

## Attack Flow
1. Attacker hosts a fake login page
2. Victim visits the page and submits credentials
3. Attacker captures them in plaintext
4. Victim sees a "Login Successful!" page

## Defense
- Always use HTTPS
- Monitor for unexpected POST requests
- Educate users about phishing risks

## License
MIT – feel free to use, modify, and share.

## Author
Ramzi 
