import ipaddress
from urllib.parse import urlparse


class PhishingDetector:

    def analyze(self, url):

        score = 0
        reasons = []

        parsed = urlparse(url)
        host = parsed.hostname or ""

        # Rule 1: HTTP instead of HTTPS
        if parsed.scheme != "https":
            score += 2
            reasons.append("Uses HTTP instead of HTTPS")

        # Rule 2: Very long URL
        if len(url) > 75:
            score += 2
            reasons.append("Very long URL")

        # Rule 3: Multiple hyphens
        if url.count("-") >= 2:
            score += 2
            reasons.append("Contains multiple hyphens")

        # Rule 4: Suspicious keywords
        keywords = [
            "login",
            "verify",
            "update",
            "secure",
            "password",
            "bank",
            "account",
            "signin",
        ]

        for word in keywords:
            if word in url.lower():
                score += 1
                reasons.append(f"Contains suspicious keyword: '{word}'")

        # Rule 5: IP Address instead of domain
        try:
            ipaddress.ip_address(host)
            score += 3
            reasons.append("Uses IP address instead of domain name")
        except ValueError:
            pass

        # Rule 6: Suspicious TLD
        bad_tlds = [
            ".xyz",
            ".top",
            ".click",
            ".zip",
            ".gq",
            ".tk",
            ".cf"
        ]

        for tld in bad_tlds:
            if host.endswith(tld):
                score += 2
                reasons.append(f"Suspicious TLD: {tld}")

        # Final Verdict
        if score <= 2:
            verdict = "✅ Safe"

        elif score <= 5:
            verdict = "⚠ Medium Risk"

        else:
            verdict = "🚨 High Risk"

        print("\n" + "=" * 50)
        print("🛡️ PHISHING URL ANALYSIS")
        print("=" * 50)

        print(f"URL        : {url}")
        print(f"Risk Score : {score}/13")
        print(f"Verdict    : {verdict}")

        print("\nReasons:")

        if reasons:
            for reason in reasons:
                print(f"✔ {reason}")
        else:
            print("✔ No suspicious indicators found.")

        print("=" * 50)

        return score, verdict, reasons