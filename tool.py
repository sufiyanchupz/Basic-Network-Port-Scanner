import socket

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except Exception as e:
        pass

def main():
    target = input("Enter target IP or domain: ")
    print(f"\nScanning target: {target}\n")

    # Common ports
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

    for port in ports:
        scan_port(target, port)

    print("\nScan completed.")

if __name__ == "__main__":
    main()