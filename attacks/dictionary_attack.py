import hashlib
import bcrypt
import time

def dictionary_attack(hash_value, hash_algo, wordlist_file="wordlist.txt"):
    start_time = time.time()
    
    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
            for word in file:
                word = word.strip()
                
                # Compute the hash based on the chosen algorithm
                if hash_algo == 'sha1':
                    word_hash = hashlib.sha1(word.encode()).hexdigest()
                elif hash_algo == 'sha224':
                    word_hash = hashlib.sha224(word.encode()).hexdigest()
                elif hash_algo == 'sha256':
                    word_hash = hashlib.sha256(word.encode()).hexdigest()
                elif hash_algo == 'sha512':
                    word_hash = hashlib.sha512(word.encode()).hexdigest()
                elif hash_algo == 'md5':
                    word_hash = hashlib.md5(word.encode()).hexdigest()
                elif hash_algo == 'bcrypt':
                    # bcrypt requires checking if the word matches the hash directly
                    if bcrypt.checkpw(word.encode(), hash_value.encode()):
                        print(f"Password found: {word}")
                        print(f"Time taken: {time.time() - start_time} seconds")
                        return word
                    continue 

                # For non-bcrypt hashes
                if word_hash == hash_value:
                    print(f"Password found: {word}")
                    print(f"Time taken: {time.time() - start_time} seconds")
                    return word

        print("Password not found in dictionary.")
    except FileNotFoundError:
        print("Wordlist file not found.")
    
    print(f"Total time taken: {time.time() - start_time} seconds")
