import subprocess
import socket

# The physical address to search for
target_physical_address = "A0-D7-68-11-0C-88"

def get_ip_address():
    try:
        # Execute the arp command
        result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
        output = result.stdout

        lines = output.split('\n')
        ip_address = ''

        # Search for the line that contains the target physical address
        for line in lines:
            if target_physical_address.lower() in line.lower():
                parts = line.split()
                ip_address = parts[0]  # The IP address is the first part of the line
                break

        # If the IP address is not found, get the IP address of the current device
        if not ip_address:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)

        return ip_address

    except Exception as e:
        print(f"Error executing arp command: {e}")
        return None

# Example usage
ip = get_ip_address()
