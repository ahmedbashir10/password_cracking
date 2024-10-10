import hashlib

# Funktion för att skapa en rainbow table
def create_rainbow_table(wordlist):
    rainbow_table = {}
    for word in wordlist:
        word_hash = hashlib.sha256(word.encode()).hexdigest()
        rainbow_table[word_hash] = word
    return rainbow_table

# Funktion för att använda rainbow table för att hitta lösenordet
def rainbow_table_attack(hash_to_crack, rainbow_table):
    return rainbow_table.get(hash_to_crack, None)

# Funktion för att köra rainbow table attack
def run():
    # Exempel på ordlista
    wordlist = ["password", "123456", "letmein", "abc123"]

    # Definiera det lösenord vi vill knäcka och skapa dess hash
    password_to_crack = "abc123"
    target_hash = hashlib.sha256(password_to_crack.encode()).hexdigest()

    # Skapa rainbow table
    rainbow_table = create_rainbow_table(wordlist)

    # Testa rainbow table attack
    result = rainbow_table_attack(target_hash, rainbow_table)

    if result:
        print(f"Lösenord funnet via rainbow table: {result}")
    else:
        print("Ingen matchning i rainbow table.")

# Om du vill köra funktionen direkt utan huvudmeny
if __name__ == "__main__":
    run()
