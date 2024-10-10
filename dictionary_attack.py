import hashlib
import time  # Importera time-biblioteket för att mäta tid

# Funktion för att läsa ordlistan från en fil (rockyou.txt)
def load_wordlist(file_path):
    with open(file_path, "r", encoding="latin-1") as f:
        return [line.strip() for line in f]

# Funktion för ordboksattack
def dictionary_attack(hash_to_crack, wordlist):
    for word in wordlist:
        #word_hash = hashlib.sha256(word.encode()).hexdigest()
        #word_hash = hashlib.md5(word.encode()).hexdigest()
        word_hash = hashlib.sha1(word.encode()).hexdigest()
 
        if word_hash == hash_to_crack:
            return word
    return None

# Funktion för att köra ordboksattacken
def run():
    print("Ordboksattacken startar...")  # Kontrollera att run() körs

    # Exempel: Hash att knäcka
    password_to_crack = "12345678"  # Du kan ändra detta för att testa andra lösenord
    #target_hash = hashlib.sha256(password_to_crack.encode()).hexdigest()  # SHA-256
    #target_hash = hashlib.md5(password_to_crack.encode()).hexdigest()  # MD5
    target_hash = hashlib.sha1(password_to_crack.encode()).hexdigest()  # SHA-1

    # Ladda ordlistan från rockyou.txt
    wordlist = load_wordlist("rockyou.txt")
    print(f"Antal ord laddade: {len(wordlist)}")

    # Mät hur lång tid attacken tar
    start_time = time.time()  # Starta tidtagning

    # Testa ordboksattacken
    result = dictionary_attack(target_hash, wordlist)

    end_time = time.time()  # Stoppa tidtagning
    print(f"Tiden det tog att knäcka lösenordet: {end_time - start_time} sekunder")

    if result:
        print(f"Lösenord funnet via ordboksattack: {result}")
    else:
        print("Ingen matchning i ordlistan.")

# Om du vill köra funktionen direkt utan huvudmeny
if __name__ == "__main__":
    run()

