import re

# Funktion för att kontrollera lösenordets komplexitet
def check_password_complexity(password):
    # Definiera komplexitetskrav
    min_length = 8
    if len(password) < min_length:
        return False, "Lösenordet måste vara minst 8 tecken långt."
    
    if not re.search(r"[A-Z]", password):
        return False, "Lösenordet måste innehålla minst en versal."
    
    if not re.search(r"[a-z]", password):
        return False, "Lösenordet måste innehålla minst en gemen."
    
    if not re.search(r"[0-9]", password):
        return False, "Lösenordet måste innehålla minst en siffra."
    
    if not re.search(r"[@$!%*?&]", password):
        return False, "Lösenordet måste innehålla minst ett specialtecken (@$!%*?&)."
    
    return True, "Lösenordet är tillräckligt säkert."

# Funktion för att köra lösenordskomplexitetskontrollen
def run():
    # Testa med några lösenord
    passwords = ["test", "Test1234", "StrongPass1!", "weakpass"]
    for pwd in passwords:
        is_valid, message = check_password_complexity(pwd)
        print(f"Lösenord: {pwd} -> {message}")

# Om du vill köra funktionen direkt utan huvudmeny
if __name__ == "__main__":
    run()

