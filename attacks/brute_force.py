# attacks/brute_force.py
import itertools
import hashlib
import time

def brute_force_attack(hash_value, max_length, charset="abcdefghijklmnopqrstuvwxyz"):
    start_time = time.time()
    print(f"Starting brute force attack on hash: {hash_value}")
    
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)
            guess_hash = hashlib.sha256(guess.encode()).hexdigest()
            
            if guess_hash == hash_value:
                print(f"Password found: {guess}")
                print(f"Time taken: {time.time() - start_time} seconds")
                return guess

    print("Password not found.")
    print(f"Total time taken: {time.time() - start_time} seconds")
