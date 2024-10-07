import hashlib  # Lägg till denna import för att kunna använda hashlib
import os  # För att generera ett slumpmässigt salt

# Funktion för att hasha ett lösenord med ett slumpmässigt salt
def hash_password(password):
    salt = os.urandom(16)  # Generera ett slumpmässigt salt (16 bytes)
    hash_value = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt, hash_value

# Funktion för att verifiera lösenordet genom att jämföra dess hash med den lagrade hashen
def verify_password(stored_salt, stored_hash, password_attempt):
    attempt_hash = hashlib.sha256(stored_salt + password_attempt.encode()).hexdigest()
    return attempt_hash == stored_hash

# Funktion för att köra hashning och verifiering
def run():
    # Exempel
    password = "securepassword"
    salt, stored_hash = hash_password(password)
    print(f"Salt: {salt}\nHash: {stored_hash}")

    # Verifiera lösenordet
    print(verify_password(salt, stored_hash, "securepassword"))  # True
    print(verify_password(salt, stored_hash, "wrongpassword"))  # False

# Om du vill köra funktionen direkt utan huvudmeny
if __name__ == "__main__":
    run()

