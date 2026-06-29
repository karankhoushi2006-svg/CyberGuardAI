class CyberGuardAI:

    def __init__(self):
        self.knowledge = {
            "hello": "Hello! I am CyberGuard AI 🛡️",
            "hi": "Hi! How can I help you today?",
            "sql injection":
                "SQL Injection is a cyber attack where malicious SQL commands are inserted into database queries.",
            "xss":
                "Cross-Site Scripting (XSS) allows attackers to inject malicious JavaScript into web pages.",
            "phishing":
                "Phishing is a social engineering attack that tricks users into revealing passwords or other sensitive information.",
            "password":
                "Use at least 12 characters, include uppercase, lowercase, numbers, and symbols.",
            "bye":
                "Goodbye! Stay safe online. 🔐",
            "firewall":
                "A firewall monitors and filters incoming and outgoing network traffic."
        }

    def get_response(self, message):
        message = message.lower()

        for key in self.knowledge:
            if key in message:
                return self.knowledge[key]

        return "Sorry, I don't know the answer yet."