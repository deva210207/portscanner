import socket

print("=" * 50)
print("          TCP PORT SCANNER")
print("=" * 50)

host = input("Enter Host (Example: localhost or 127.0.0.1): ")

try:
    target_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("Invalid Host!")
    exit()

print(f"\nScanning {target_ip}...\n")

start_port = int(input("Enter Starting Port: "))
end_port = int(input("Enter Ending Port: "))

print("\nOpen Ports:")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target_ip, port))

    if result == 0:
        print(f"Port {port} : OPEN")

    sock.close()

print("\nScan Completed.")
