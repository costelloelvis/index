import socket

def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(50)  # Set timeout for the connection
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target_host = "127.0.0.1"  # Replace with your target IP address
    port_range = range(1, 1025)  # Scan ports from 1 to 1024
    
    print(f"Scanning ports on {target_host}...")
    open_ports = scan_ports(target_host, port_range)
    
    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")
