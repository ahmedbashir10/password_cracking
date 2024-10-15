# main.py
import argparse
from attacks.brute_force_attack import brute_force_hashed_with_salt, brute_force_hashed_no_salt, brute_force_plaintext, optimized_brute_force_hashed
from attacks.dictionary_attack import dictionary_attack
from attacks.rainbow_table_attacks import rainbow_table_attack
from attacks.rainbow_table_attacks import generate_rainbow_table
from utils.hashing import hash_password, hash_password_with_salt
from utils.password_complexity_check import check_password_strength


def main():
    parser = argparse.ArgumentParser(description="Password Cracking Program")
    
    # CLI arguments
    parser.add_argument('--password', type=str, help='The password to crack or hash')
    parser.add_argument('--hash', type=str, help='Hash value of the password (if provided)')
    parser.add_argument('--attack', type=str, choices=['brute_force', 'dictionary'], help='The attack method to use')
    parser.add_argument('--hash_algo', type=str, choices=['sha256', 'bcrypt'], default='sha256', help='Hashing algorithm to use')
    parser.add_argument('--max_length', type=int, default=5, help='Maximum password length for brute force')
    parser.add_argument('--salt', type=str, help='Salt value for hashing (if provided)')
    parser.add_argument('--dictionary', type=str, help='Path to the dictionary file')
    parser.add_argument('--terminal', help="Display table with port forwarding data.", nargs="?", const=True,)
    
    args = parser.parse_args()



    if args.terminal: 
        print("Choose which attack or protection mechanism you want to test:")
        print("1. Enter your password!")
        print("2. Attacks!")
        print("3. Protection Mechanisms!")
        print("4. Exit")
        
        choice = input("Enter the number for your choice: ")

        if choice == "1": 
            print("1. Hash the password")
            print("2. Hash the password with salt!")
            print("3. Without hashed the password")
            print("4. Exit")
            print("\n")

            choice = input("Enter the number for your choice: ")

            if choice == "1":
                print("Hash the password! Choose the hashing algorithm.")
                print("1. Sha1")
                print("2. Sha224")
                print("3. Sha256")
                print("4. sha512")
                print("5. md5")
                print("6. bcrypt")
                print("7. Exit")

                choice = input("Enter the number for your choice: ")

                if choice == "1":
                    print("Sha1 hashing algorithm!")
                    hash_algo = "sha1" 
                    password = input("Enter your password: ")
                    hash_value = hash_password(password, hash_algo)
                    print(hash_value)
                elif choice == "2":
                    print("Sha224 hashing algorithm!")
                    hash_algo = "sha224" 
                    password = input("Enter your password: ")
                    hash_value = hash_password(password, hash_algo)
                    print(hash_value)
                elif choice == "3":
                    print("Sha256 hashing algorithm!")
                    hash_algo = "sha256" 
                    password = input("Enter your password: ")
                    hash_value = hash_password(password, hash_algo)
                    print(hash_value)
                elif choice == "4":
                    print("Sha512 hashing algorithm!")
                    hash_algo = "sha512" 
                    password = input("Enter your password: ")
                    hash_value = hash_password(password, hash_algo)
                    print(hash_value)
                elif choice == "5":
                    print("Md5 hashing algorithm!")
                    hash_algo = "md5" 
                    password = input("Enter your password: ")
                    hash_value = hash_password(password, hash_algo)
                    print(hash_value)
                elif choice == "6":
                    print("Bcrypt hashing algorithm!")
                    hash_algo = "bcrypt" 
                    password = input("Enter your password: ")
                    hash_value = hash_password(password, hash_algo)
                    print(hash_value)
                elif choice == "7":
                    print("Exit!")
                    exit()

            elif choice == "2":
                print("Hash the password! Choose the hashing algorithm with salt.")
                print("1. Sha1")
                print("2. Sha224")
                print("3. Sha256")
                print("4. Sha512")
                print("5. md5")
                print("6. bcrypt")
                print("7. Exit")

                choice = input("Enter the number for your choice: ")

                if choice == "1":
                    print("Sha1 hashing algorithm!")
                    hash_algo = "sha1" 
                    password = input("Enter your password: ")
                    hash_value = hash_password_with_salt(password, hash_algo)
                    print(hash_value[0])
                elif choice == "2":
                    print("Sha224 hashing algorithm!")
                    hash_algo = "sha224"
                    password = input("Enter your password: ")
                    hash_value = hash_password_with_salt(password, hash_algo)
                    print(hash_value[0])
                elif choice == "3": 
                    print("Sha256 hashing algorithm!")
                    hash_algo = "sha256" 
                    password = input("Enter your password: ")
                    hash_value = hash_password_with_salt(password, hash_algo)
                    print(hash_value[0])
                elif choice == "4":
                    print("Sha512 hashing algorithm!")
                    hash_algo = "sha512" 
                    password = input("Enter your password: ")
                    hash_value = hash_password_with_salt(password, hash_algo)
                    print(hash_value[0])
                elif choice == "5":
                    print("Md5 hashing algorithm!")
                    hash_algo = "md5" 
                    password = input("Enter your password: ")
                    hash_value = hash_password_with_salt(password, hash_algo)
                    print(hash_value[0])
                elif choice == "6":
                    print("Bcrypt hashing algorithm!")
                    hash_algo = "bcrypt" 
                    password = input("Enter your password: ")
                    hash_value = hash_password_with_salt(password, hash_algo)
                    print(hash_value[0])
                elif choice == "7":
                    print("Exit!")
                    exit()

            elif choice == "3":
                print("Without hashed the password!")
                password = input("Enter your password: ")
                print(password)
            elif choice == "4":
                print("Exit!")
                exit()
            elif choice is None or int(choice) >= 4:
                print("Wrong choice! Please choose a correct choice.")


        elif choice == "2":
            print("Choose an attack method:")
            print("1. Brute Force Attack")
            print("2. Dictionary Attack")
            print("3. Rainbow Table Attack")
            choice = input("Enter the number for your choice: ")

            if choice == "1": 
                print("Brute force attack!")
                print("1. Brute force with plaintext")
                print("2. Brute force with no salt")
                print("3. Brute force with with salt")
                print("4. Brute force with optimization")
                print("5. Exit")
                choice = input("Enter the number for your choice: ")

                if choice == "1":
                    print("Brute force with plaintext!")
                    print("Started brute force-attack...")
                    target_hash = input("Enter the target password: ")
                    max_length = int(input("Enter the maximum password length: "))
                    result = brute_force_plaintext(target_hash, max_length)
                    print(result)
                elif choice == "2":
                    print("Brute force with no salt!")
                    print("Started brute force-attack...")
                    target_hash = input("Enter the target password: ")
                    max_length = int(input("Enter the maximum password length: "))
                    algorithm = input("Enter the hashing algorithm: ")
                    result = brute_force_hashed_no_salt(target_hash, max_length, algorithm)
                    print(result)
                elif choice == "3":
                    print("Brute force with with salt!")
                    print("Started brute force-attack...")
                    target_hash = input("Enter the target password: ")
                    max_length = int(input("Enter the maximum password length: "))
                    algorithm = input("Enter the hashing algorithm: ")
                    result = brute_force_hashed_with_salt(target_hash, max_length, algorithm)
                    print(result)
                elif choice == "4":
                    print("Brute force with optimization!")
                    print("Started brute force-attack...")
                    target_hash = input("Enter the target password: ")
                    max_length = int(input("Enter the maximum password length: "))
                    algorithm = input("Enter the hashing algorithm: ")
                    result = optimized_brute_force_hashed(target_hash, max_length, algorithm)
                    print(result)
                elif choice == "5":
                    print("Exit!")
                    exit()
                elif choice is None or int(choice) >= 5:
                    print("Wrong choice! Please choose a correct choice.")
                
            elif choice == "2":
                print("Dictionary attack!")
                print("Started the attack...")
                target_hash = input("Enter the target password: ")
                algorithm = input("Enter the hashing algorithm: ")
                result = dictionary_attack(target_hash, algorithm)
                print(result)
            elif choice == "3":
                print("Rainbow attack!")
                print("Started the attack...")
                target_hash = input("Enter the target password: ")
                algorithm = input("Enter the hashing algorithm: ")
                rainbow_table = generate_rainbow_table(algorithm)
                print("Generated the rainbow table")
                result = rainbow_table_attack(target_hash, rainbow_table)
                print(result)
            elif choice == "4":
                print("Hash with salt attack!")
        
        elif choice == "3":
            print("Protection mechanisms!")
            password = input("Enter your password to check its strength: ")
            feedback = check_password_strength(password, wordlist="wordlist.txt")
            print(feedback)
        elif choice is None or int(choice) >= 4:
            print("Wrong choice! Please choose a correct choice.")

    else: 
        print("Please provide a valid attack method and hash")

if __name__ == "__main__":
    main()
