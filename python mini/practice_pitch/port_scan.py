import socket

def port_scanner(target, ports):
    clcoding = socket.gethostbyname(target)
    print(f"Scanning {target}({google})")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((clcoding, port))
        if result == o:
            print(f"Port {port}: Open")

        sock.close()

target = "clcoding.com"
ports = [22, 443, 80, 8080]
port_scanner(target, ports)
