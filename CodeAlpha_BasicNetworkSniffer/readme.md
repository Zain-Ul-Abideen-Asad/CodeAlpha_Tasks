# Basic Network Sniffer
CodeAlpha Cybersecurity Internship – Task 1

## Project Overview
This project is a basic network sniffer developed using Python and the Scapy library on Kali Linux.
The program captures live network packets and analyzes them to understand how data flows through a network.

This project was completed as part of the Cybersecurity Internship at CodeAlpha.

## Tools & Technologies
- Operating System: Kali Linux (VMware Workstation Pro 17.5)
- Programming Language: Python 3
- Library Used: Scapy

## Features
- Captures live network traffic
- Displays source and destination IP addresses
- Identifies network protocols (TCP, UDP, ICMP)
- Displays source and destination ports
- Shows packet payload when available

## How It Works
The sniffer uses Scapy’s sniff() function to capture live network traffic.
Each captured packet is analyzed to extract key information such as IP addresses, protocol type, ports, and payload data.

## Sample Output
Source IP : <REDACTED>
Destination IP : <REDACTED>
Protocol : TCP
Source Port : 443
Destination Port: <DYNAMIC_PORT>
Payload : <ENCRYPTED_DATA>

## Encryption Observation
Most modern web traffic uses HTTPS, which encrypts data using TLS.
As a result, the payload appears unreadable.
This demonstrates how packet sniffers can analyze packet metadata but cannot decrypt encrypted traffic.

## Ethical Considerations
This project was developed and tested in a controlled lab environment for educational purposes only.
Packet sniffing should only be performed on networks that you own or have explicit permission to monitor.

## How to Run
```bash
sudo python3 sniffer.py
