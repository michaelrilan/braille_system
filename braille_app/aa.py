import subprocess
import re
import uuid
import socket

def get_local_ip():
    # Create a socket connection
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Connect to an external server to determine the local IP address
        s.connect(("8.8.8.8", 80))  # Google Public DNS server
        local_ip = s.getsockname()[0]
    return local_ip



def get_mac_address():
    # Get the MAC address from the UUID
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    return mac


def get_arp_table():
    # Run 'arp -a' command and capture the output
    result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    return result.stdout

def find_ip_for_mac(arp_output, target_mac_address):
    # Regular expression pattern to match IP and MAC addresses
    pattern = re.compile(r"(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F:-]+)\s+(\w+)")
    
    # Search for the MAC address in the ARP table
    for ip, mac, _ in pattern.findall(arp_output):
        if mac.lower() == target_mac_address.lower():
            return ip
    return None

# MAC address to search for
target_mac_address = get_mac_address()
target_mac_address = target_mac_address.lower()

# Get ARP table
arp_output = get_arp_table()

# Find IP address for the given MAC address
ip_address = find_ip_for_mac(arp_output, target_mac_address)

if ip_address:
    print(f"py manage.py runserver {ip_address}:4040")
else:
    print(f"MAC address {target_mac_address} does not exist.")



print(f"MAC address: {target_mac_address}")

# Get local IP address
local_ip = get_local_ip()
print(f"Local IP address: {local_ip}")
