from chatbot import CyberGuardAI
from password_checker import PasswordChecker

bot = CyberGuardAI()
checker = PasswordChecker()

print("=" * 50)
print("🛡️ Welcome to CyberGuard AI")
print("=" * 50)

while True:

    user = input("\nYou : ")

    if user.lower() == "exit":
        print("Bot : Thank you for using CyberGuard AI.")
        break

    if user.lower() == "check password":

        password = input("Enter password: ")

        strength, suggestions = checker.check_strength(password)

        print("\nPassword Strength:", strength)

        if suggestions:
            print("\nSuggestions:")
            for suggestion in suggestions:
                print("-", suggestion)

        continue

    response = bot.get_response(user)

    print("Bot :", response)