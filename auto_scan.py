import sys
import subprocess
import xml.etree.ElementTree as ET

target_ip = sys.argv[1]

print(f"\n Scanning target: {target_ip}\n")

subprocess.run([
    "nmap","-Pn","-sS", "-sV", "-oX", "scan.xml", target_ip
])

tree = ET.parse("scan.xml")
root = tree.getroot()

risk_map = {
    "21":  ("ftp", "High – Cleartext credentials, brute-force risk"),
    "22":  ("ssh", "Medium – Brute-force and credential abuse"),
    "23":  ("telnet", "High – Unencrypted remote access"),
    "80":  ("http", "Medium – Web service exposure"),
    "135": ("msrpc", "Low – RPC service exposure"),
    "139": ("netbios-ssn", "Medium – NetBIOS enumeration risk"),
    "445": ("microsoft-ds", "High – SMB exploitation & lateral movement"),
    "3389": ("rdp", "High – RDP brute-force & exploitation"),
    "8080": ("http-proxy", "Medium – Web service on non-standard port")
}


print("\n Security Risk Report\n")

open_port_found = False

for host in root.findall("host"):
    for port in host.iter("port"):

            if state == "open":
               open_port_found = True

               port_id = port.get("portid")
               protocol = port.get("protocol")

               service = port.find("service")
               service_name = service.get("name") if service is not None else "unknown"

               risk = risk_map.get(port_id, "No common risk identified")

               print(f"""
               Port    : {port_id}/{protocol}
               Service : {service_name }
               Risk    : {risk}
               """)
if not open_port_found:
    print("No open ports were detected on the target.")
