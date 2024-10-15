# attacks/rainbow_table.py
import hashlib
import time

# Generate a rainbow table based on a wordlist
def generate_rainbow_table(hash_algo, wordlist_file="wordlist.txt"):
    rainbow_table = {}

    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
            for word in file:
                word = word.strip()
                
                if hash_algo == 'sha256':
                    hash_value = hashlib.sha256(word.encode()).hexdigest()
                elif hash_algo == 'md5':
                    hash_value = hashlib.md5(word.encode()).hexdigest()
                elif hash_algo == 'sha1':
                    hash_value = hashlib.sha1(word.encode()).hexdigest()
                elif hash_algo == 'sha224':
                    hash_value = hashlib.sha224(word.encode()).hexdigest()
                elif hash_algo == 'sha512':
                    hash_value = hashlib.sha512(word.encode()).hexdigest()

                rainbow_table[hash_value] = word

        return rainbow_table

    except FileNotFoundError:
        print("Wordlist file not found.")


def rainbow_table_attack(hash_value, rainbow_table):
    start_time = time.time()

    # Check if the hash is in the rainbow table
    if hash_value in rainbow_table:
        print(f"Password found: {rainbow_table[hash_value]}")
        print(f"Time taken: {time.time() - start_time} seconds")
        return rainbow_table[hash_value]
    else:
        print("Password not found in the rainbow table.")
    
    print(f"Total time taken: {time.time() - start_time} seconds")
