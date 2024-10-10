import brute_force_attack
import dictionary_attack
import rainbow_table_attack
import hashing_with_salt
import password_complexity_check
import rate_limiting_and_captcha

def main_menu():
    print("Välj vilken attack eller skyddsmekanism du vill testa:")
    print("1. Brute Force Attack")
    print("2. Ordboksattack")
    print("3. Rainbow Table Attack")
    print("4. Hashing med Salt")
    print("5. Lösenordskomplexitetskontroll")
    print("6. Rate Limiting och CAPTCHA-simulering")
    choice = input("Skriv numret för ditt val: ")

    if choice == "1":
        brute_force_attack.run()
    elif choice == "2":
        dictionary_attack.run()  # Anropar `run()` i dictionary_attack.py
    elif choice == "3":
        rainbow_table_attack.run()
    elif choice == "4":
        hashing_with_salt.run()
    elif choice == "5":
        password_complexity_check.run()
    elif choice == "6":
        rate_limiting_and_captcha.run()
    else:
        print("Ogiltigt val!")

if __name__ == "__main__":
    main_menu()

