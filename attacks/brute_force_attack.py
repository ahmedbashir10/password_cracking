import itertools
import hashlib
import bcrypt
import time

import argparse

def brute_force_plaintext(target_password, max_length, charset="abcdefghijklmnopqrstuvwxyz"):
    start_time = time.time()
    print(f"Starting brute force attack without hashing on target password: {target_password}")

    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)
            if guess == target_password:
                end_time = time.time()
                print(f"Password found: {guess}")
                print(f"Time taken: {end_time - start_time} seconds")
                return guess

    print("Password not found.")
    print(f"Total time taken: {time.time() - start_time} seconds")



def brute_force_hashed_no_salt(hash_value, max_length, hash_algo, charset="abcdefghijklmnopqrstuvwxyz"):
    start_time = time.time()
    print(f"Starting brute force attack on hash: {hash_value} with algorithm: {hash_algo}")

    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)

            # Hash the guess without salt
            if hash_algo == "sha256":
                guess_hash = hashlib.sha256(guess.encode()).hexdigest()
            elif hash_algo == "md5":
                guess_hash = hashlib.md5(guess.encode()).hexdigest()
            elif hash_algo == "bcrypt":
                guess_hash = bcrypt.hashpw(guess.encode())
            # Add more algorithms as needed...

            if guess_hash == hash_value:
                end_time = time.time()
                print(f"Password found: {guess}")
                print(f"Time taken: {end_time - start_time} seconds")
                return guess

    print("Password not found.")
    print(f"Total time taken: {time.time() - start_time} seconds")



def brute_force_hashed_with_salt(hash_value, salt, max_length, hash_algo, charset="abcdefghijklmnopqrstuvwxyz"):
    start_time = time.time()
    print(f"Starting brute force attack on hash: {hash_value} with algorithm: {hash_algo} and salt")

    salt = str(salt).encode()  # Ensure the salt is in byte form

    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)

            # Hash the guess with salt
            if hash_algo == "sha256":
                guess_hash = hashlib.sha256(salt + guess.encode()).hexdigest()
            elif hash_algo == "md5":
                guess_hash = hashlib.md5(salt + guess.encode()).hexdigest()
            elif hash_algo == "bcrypt":
                guess_hash = bcrypt.hashpw(guess.encode(), bcrypt.gensalt())

            if guess_hash == hash_value:
                end_time = time.time()
                print(f"Password found: {guess}")
                print(f"Time taken: {end_time - start_time} seconds")
                return guess

    print("Password not found.")
    print(f"Total time taken: {time.time() - start_time} seconds")



def optimized_brute_force_hashed(hash_value, max_length, hash_algo, charset="abcdefghijklmnopqrstuvwxyz"):
    start_time = time.time()
    print(f"Starting optimized brute force attack on hash: {hash_value} with algorithm: {hash_algo}")

    # Heuristic: Let's assume users commonly use digits at the end of passwords
    for length in range(1, max_length + 1):
        for prefix in itertools.product(charset, repeat=length - 1):
            for suffix in itertools.product("0123456789", repeat=1):
                guess = ''.join(prefix) + ''.join(suffix)

                # Hash the guess
                if hash_algo == "sha256":
                    guess_hash = hashlib.sha256(guess.encode()).hexdigest()
                elif hash_algo == "md5":
                    guess_hash = hashlib.md5(guess.encode()).hexdigest()
                elif hash_algo == "bcrypt":
                    guess_hash = bcrypt.hashpw(guess.encode(), bcrypt.gensalt())
                # Add more algorithms as needed...

                if guess_hash == hash_value:
                    end_time = time.time()
                    print(f"Password found: {guess}")
                    print(f"Time taken: {end_time - start_time} seconds")
                    return guess

    print("Password not found.")
    print(f"Total time taken: {time.time() - start_time} seconds")





def main():
    parser = argparse.ArgumentParser(description="Test brute force password cracking functions")
    
    # CLI arguments
    parser.add_argument('--mode', type=str, choices=['plaintext', 'hashed_no_salt', 'hashed_with_salt', 'optimized'], help='The brute force mode to test')
    parser.add_argument('--password', type=str, help='The target password for plaintext brute force')
    parser.add_argument('--hash_value', type=str, help='The hash value to brute force')
    parser.add_argument('--salt', type=str, help='The salt value (for salted hashing attacks)')
    parser.add_argument('--max_length', type=int, default=5, help='Maximum password length for brute force')
    parser.add_argument('--hash_algo', type=str, choices=['sha256', 'md5', 'bcrypt'], default='sha256', help='Hashing algorithm to use')
    parser.add_argument('--charset', type=str, default="abcdefghijklmnopqrstuvwxyz", help='Charset to use for brute force')

    args = parser.parse_args()

    if args.mode == 'plaintext':
        if not args.password:
            print("Please provide the --password argument for plaintext mode.")
        else:
            brute_force_plaintext(args.password, args.max_length, args.charset)

    elif args.mode == 'hashed_no_salt':
        if not args.hash_value:
            print("Please provide the --hash_value argument for hashed_no_salt mode.")
        else:
            brute_force_hashed_no_salt(args.hash_value, args.max_length, args.hash_algo, args.charset)

    elif args.mode == 'hashed_with_salt':
        if not args.hash_value or not args.salt:
            print("Please provide the --hash_value and --salt arguments for hashed_with_salt mode.")
        else:
            brute_force_hashed_with_salt(args.hash_value, args.salt, args.max_length, args.hash_algo, args.charset)

    elif args.mode == 'optimized':
        if not args.hash_value:
            print("Please provide the --hash_value argument for optimized mode.")
        else:
            optimized_brute_force_hashed(args.hash_value, args.max_length, args.hash_algo, args.charset)

if __name__ == "__main__":
    main()