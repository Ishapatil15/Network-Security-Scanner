Network Security Scanner (Python + Nmap)

Overview
This project is a **Python-based automated network security scanner** that uses **Nmap** to identify open ports, running services, and potential security risks on a target system within a local network.

The goal of this project is to understand **real-world network reconnaissance**, port scanning, and basic **risk assessment**, which are core concepts in cybersecurity and penetration testing.

---

 Tools & Technologies Used
- **Kali Linux**
- **Python 3**
- **Nmap**
- **VirtualBox (Host-only + NAT networking)**
- **Windows VM (target machine)**

---

How the Project Works
1. The user provides a **target IP address**.
2. The Python script executes an **Nmap service/version scan**.
3. Open ports and services are extracted from the scan output.
4. Each detected service is mapped to a **basic security risk**.
5. A **readable security report** is displayed in the terminal.

This makes the scanner dynamic, as results depend on the actual network state of the target machine.





