import re

def load_wordlist(file_path):
    try:
        with open(file_path, 'r') as file:
            wordlist = set(file.read().splitlines())
        return wordlist
    except FileNotFoundError:
        print("Wordlist file not found. Skipping wordlist check.")
        return set()

def check_password_strength(password, wordlist):
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'[0-9]', password)
    has_special = re.search(r'[\W_]', password)
    
    length = len(password)

    if password in wordlist:
        return "Weak Password: Password is too common. Avoid using passwords from known wordlists."

    # The password is weak if less than 6 character
    if length < 6:
        return "Weak Password: Password is too short."

    # The password is medium between 6 to 10 characters
    if 6 <= length <= 10:
        if any([has_upper, has_lower, has_digit, has_special]):
            return "Medium Password: Could be stronger by adding more characters and complexity."
    
    # The password is strong more than 10 character
    if length > 10 and all([has_upper, has_lower, has_digit, has_special]):
        return "Strong Password: Password meets length and complexity requirements."
    
    # If length > 10 but missing some complexity, still consider it medium
    if length > 10:
        return "Medium Password: Add more complexity (use a mix of upper/lowercase, digits, and special characters)."

    # Fallback
    return "Weak Password: Needs more characters or complexity."

#def main():
 #   password = input("Enter your password to check its strength: ")

  #  wordlist = load_wordlist("wordlist.txt")
    
   # feedback = check_password_strength(password, wordlist)
    #print(feedback)

#if __name__ == "__main__":
 #   main()
