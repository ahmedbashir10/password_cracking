# main.py
import argparse
from attacks.brute_force import brute_force_attack
from attacks.dictionary_attack import dictionary_attack
from utils.hashing import hash_password

def main():
    parser = argparse.ArgumentParser(description="Password Cracking Program")
    
    # CLI arguments
    parser.add_argument('--password', type=str, help='The password to crack or hash')
    parser.add_argument('--hash', type=str, help='Hash value of the password (if provided)')
    parser.add_argument('--attack', type=str, choices=['brute_force', 'dictionary'], help='The attack method to use')
    parser.add_argument('--hash_algo', type=str, choices=['sha256', 'bcrypt'], default='sha256', help='Hashing algorithm to use')
    parser.add_argument('--max_length', type=int, default=5, help='Maximum password length for brute force')
    
    args = parser.parse_args()

    # Hash the password if provided
    if args.password and not args.hash:
        hashed_password = hash_password(args.password, args.hash_algo)
        print(f"Hashed password: {hashed_password}")

    # Call the appropriate attack method
    if args.attack == 'brute_force' and args.hash:
        brute_force_attack(args.hash, args.max_length)
    elif args.attack == 'dictionary' and args.hash:
        dictionary_attack(args.hash)
    else:
        print("Please provide a valid attack method and hash.")

if __name__ == "__main__":
    main()
