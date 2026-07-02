import whois


class WhoisLookup:

    def lookup(self):

        domain = input("Enter Domain : ")

        try:

            data = whois.whois(domain)

            print("\n" + "=" * 50)
            print("🌍 WHOIS LOOKUP")
            print("=" * 50)

            print("Domain      :", data.domain_name)
            print("Registrar   :", data.registrar)
            print("Created On  :", data.creation_date)
            print("Expires On  :", data.expiration_date)
            print("Name Server :", data.name_servers)

            print("=" * 50)

        except Exception as e:

            print("Error :", e)