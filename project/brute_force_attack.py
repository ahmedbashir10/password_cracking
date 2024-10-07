import itertools
import hashlib

# Funktion som testar en brute force attack
def brute_force_attack(hash_to_crack, charset, max_length):
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)
            guess_hash = hashlib.sha256(guess.encode()).hexdigest()
            if guess_hash == hash_to_crack:
                return guess
    return None

# Funktion som kör brute force attacken
def run():
    # Exempel: Hash att knäcka (hashad version av "abc123")
    target_hash = hashlib.sha256("abc123".encode()).hexdigest()
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'

    # Max längd på lösenordet som ska testas
    max_length = 6

    print("Startar brute force-attack...")
    result = brute_force_attack(target_hash, charset, max_length)

    if result:
        print(f"Lösenord funnet: {result}")
    else:
        print("Ingen matchning hittad.")
if __name__ == "__main__":
    run()

