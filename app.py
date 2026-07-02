from chatbot import CyberGuardAI
from password_checker import PasswordChecker
from phishing_detector import PhishingDetector
from hash_generator import HashGenerator
from port_scanner import PortScanner
from dns_lookup import DNSLookup
from whois_lookup import WhoisLookup

bot = CyberGuardAI()
checker = PasswordChecker()
detector = PhishingDetector()
hash_gen = HashGenerator()
scanner = PortScanner()
dns = DNSLookup()
whois_tool = WhoisLookup()

print("=" * 50)
print("🛡️ Welcome to CyberGuard AI")
print("=" * 50)

while True:

    user = input("\nYou : ").lower()

    if user == "exit":
        print("Bot : Thank you for using CyberGuard AI.")
        break

    elif user == "check password":

        password = input("Enter Password : ")

        strength, suggestions = checker.check_strength(password)

        print("\nPassword Strength :", strength)

        if suggestions:
            print("\nSuggestions:")
            for suggestion in suggestions:
                print("-", suggestion)

    elif user == "check url":

        url = input("Enter URL : ")

        detector.analyze(url)
    
    elif user == "hash":

        text = input("Enter Text : ")

        hash_gen.generate_hashes(text)

    elif user == "scan port":

        scanner.scan()
    elif user == "dns":

        dns.lookup()
        
    elif user == "whois":

        whois_tool.lookup()

        
    else:

        print("Bot :", bot.get_response(user))