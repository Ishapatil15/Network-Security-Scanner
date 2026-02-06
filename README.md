🔐 **Automated Vulnerability Network Scanner**

An automated Python-based network vulnerability scanner that performs port scanning, service detection, and risk analysis using Nmap and XML parsing.

1.Overview

  This project scans a target IP address, identifies open ports and running services, and maps them to predefined security risks. It automates basic vulnerability assessment and generates a structured security      risk report.
  
  Developed as a practical cybersecurity implementation project using Kali Linux.

2.Features

 -TCP SYN Scan (-sS)
 
 -Service Version Detection (-sV)
 
 -Host Discovery Bypass (-Pn)
 
 -Automatic XML Parsing of Nmap Results
 
 -Detection of Open Ports
 
 -Predefined Risk Classification Mapping
 
 -Structured Terminal-Based Security Report

3. Tools & Technologies Used
   
- Kali Linux
- Python 3
- Nmap
- VirtualBox (Host-only + NAT networking)
- Windows VM (target machine)

---

How the Project Works
1. The user provides a **target IP address**.
2. The Python script executes an **Nmap service/version scan**.
3. Open ports and services are extracted from the scan output.
4. Each detected service is mapped to a **basic security risk**.
5. A **readable security report** is displayed in the terminal.
   

This makes the scanner dynamic, as results depend on the actual network state of the target machine.

**Disclaimer**
This tool is developed strictly for educational and ethical security testing purposes. Unauthorized scanning of networks is illegal.





