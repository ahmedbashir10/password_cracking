# attacks/dictionary_attack.py
import hashlib
import time

def dictionary_attack(hash_value, wordlist_file="wordlist.txt"):
    start_time = time.time()
    
    try:
        with open(wordlist_file, 'r') as file:
            for word in file:
                word = word.strip()
                word_hash = hashlib.sha256(word.encode()).hexdigest()
                
                if word_hash == hash_value:
                    print(f"Password found: {word}")
                    print(f"Time taken: {time.time() - start_time} seconds")
                    return word

        print("Password not found in dictionary.")
    except FileNotFoundError:
        print("Wordlist file not found.")
    
    print(f"Total time taken: {time.time() - start_time} seconds")
