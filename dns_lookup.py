import socket


class DNSLookup:

    def lookup(self):

        domain = input("Enter Domain : ")

        try:

            ip = socket.gethostbyname(domain)

            hostname = socket.getfqdn(domain)

            print("\n" + "="*50)
            print("🌐 DNS LOOKUP")
            print("="*50)

            print("Domain   :", domain)
            print("IP       :", ip)
            print("Hostname :", hostname)

            print("="*50)

        except Exception:

            print("\nInvalid Domain")