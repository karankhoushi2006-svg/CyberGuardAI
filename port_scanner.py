import socket
import time
import os


class PortScanner:

    def __init__(self):
        self.services = {
            20: "FTP Data",
            21: "FTP",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            143: "IMAP",
            443: "HTTPS",
            3306: "MySQL"
        }

    def scan(self):

        host = input("Enter Host : ")

        try:
            ip = socket.gethostbyname(host)

        except socket.gaierror:

            print("\n❌ Invalid Host\n")
            return

        start_port = int(input("Start Port : "))
        end_port = int(input("End Port   : "))

        open_ports = []

        print("\n" + "=" * 55)
        print("🛡️ CYBERGUARD AI - PORT SCANNER")
        print("=" * 55)

        print("Target :", host)
        print("IP     :", ip)
        print()

        start = time.time()

        for port in range(start_port, end_port + 1):

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((ip, port))

            if result == 0:

                service = self.services.get(port, "Unknown")

                print(f"✅ Port {port:<5} OPEN   ({service})")

                open_ports.append((port, service))

            sock.close()

        end = time.time()

        print("\n" + "=" * 55)
        print("Scan Finished")
        print(f"Time Taken : {round(end-start,2)} sec")
        print(f"Open Ports : {len(open_ports)}")
        print("=" * 55)

        self.save_report(host, ip, open_ports, end-start)

    def save_report(self, host, ip, open_ports, scan_time):

        os.makedirs("reports", exist_ok=True)

        filename = f"reports/{host}_scan.txt"

        with open(filename, "w") as file:

            file.write("CYBERGUARD AI PORT SCAN REPORT\n")
            file.write("=" * 40 + "\n")

            file.write(f"Target : {host}\n")
            file.write(f"IP     : {ip}\n")
            file.write(f"Time   : {round(scan_time,2)} sec\n\n")

            file.write("OPEN PORTS\n")
            file.write("-" * 40 + "\n")

            if open_ports:

                for port, service in open_ports:

                    file.write(f"{port} -> {service}\n")

            else:

                file.write("No Open Ports Found\n")

        print(f"\n📄 Report Saved : {filename}")