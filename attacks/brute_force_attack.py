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
            if hash_algo == "sha1":
                guess_hash = hashlib.sha1(guess.encode()).hexdigest()
            elif hash_algo == "sha224":
                guess_hash = hashlib.sha224(guess.encode()).hexdigest()
            elif hash_algo == "sha256":
                guess_hash = hashlib.sha256(guess.encode()).hexdigest()
            elif hash_algo == "sha512":
                guess_hash = hashlib.sha512(guess.encode()).hexdigest()
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
            if hash_algo == "sha1":
                guess_hash = hashlib.sha1(salt + guess.encode()).hexdigest()
            elif hash_algo == "sha224":
                guess_hash = hashlib.sha224(salt + guess.encode()).hexdigest()
            elif hash_algo == "sha256":
                guess_hash = hashlib.sha256(salt + guess.encode()).hexdigest()
            elif hash_algo == "sha512":
                guess_hash = hashlib.sha512(salt + guess.encode()).hexdigest()
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
                if hash_algo == "sha1":
                    guess_hash = hashlib.sha1(guess.encode()).hexdigest()
                elif hash_algo == "sha224":
                    guess_hash = hashlib.sha224(guess.encode()).hexdigest()
                elif hash_algo == "sha256":
                    guess_hash = hashlib.sha256(guess.encode()).hexdigest()
                elif hash_algo == "sha512":
                    guess_hash = hashlib.sha512(guess.encode()).hexdigest()
                elif hash_algo == "md5":
                    guess_hash = hashlib.md5(guess.encode()).hexdigest()
                elif hash_algo == "bcrypt":
                    guess_hash = bcrypt.hashpw(guess.encode(), bcrypt.gensalt())

                if guess_hash == hash_value:
                    end_time = time.time()
                    print(f"Password found: {guess}")
                    print(f"Time taken: {end_time - start_time} seconds")
                    return guess

    print("Password not found.")
    print(f"Total time taken: {time.time() - start_time} seconds")
