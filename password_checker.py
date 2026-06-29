import re


class PasswordChecker:

    def check_strength(self, password):
        score = 0
        suggestions = []

        # Length
        if len(password) >= 12:
            score += 1
        else:
            suggestions.append("Use at least 12 characters.")

        # Uppercase
        if re.search(r"[A-Z]", password):
            score += 1
        else:
            suggestions.append("Add at least one uppercase letter.")

        # Lowercase
        if re.search(r"[a-z]", password):
            score += 1
        else:
            suggestions.append("Add at least one lowercase letter.")

        # Number
        if re.search(r"\d", password):
            score += 1
        else:
            suggestions.append("Add at least one number.")

        # Special Character
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
        else:
            suggestions.append("Add at least one special character.")

        if score <= 2:
            strength = "Weak ❌"
        elif score == 3 or score == 4:
            strength = "Medium ⚠️"
        else:
            strength = "Strong ✅"

        return strength, suggestions