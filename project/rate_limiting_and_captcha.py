import time

# En simpel rate limiting funktion
attempts = {}
MAX_ATTEMPTS = 5
TIME_WINDOW = 60  # 60 sekunder mellan försök

def login(username, password):
    current_time = time.time()
    
    if username in attempts:
        # Rensa gamla försök som ligger utanför tidsfönstret
        attempts[username] = [t for t in attempts[username] if current_time - t < TIME_WINDOW]
        
        if len(attempts[username]) >= MAX_ATTEMPTS:
            print("För många försök, försök igen senare.")
            return False

    # Simulera att vi kollar lösenordet (här kan du lägga till en riktig kontroll)
    if password == "rättlösenord":
        print("Inloggning lyckades!")
        attempts[username] = []  # Nollställ försök om inloggningen lyckas
        return True
    else:
        print("Fel lösenord.")
        attempts.setdefault(username, []).append(current_time)
        return False

# Funktion för att testa rate limiting
def run():
    # Testa funktionen med en användare
    for i in range(7):  # Simulerar 7 inloggningsförsök
        login("användare", "fel lösenord")  # Fel lösenord varje gång
        time.sleep(10)  # Simulera 10 sekunders mellanrum mellan försök

# Om du vill köra funktionen direkt utan huvudmeny
if __name__ == "__main__":
    run()

