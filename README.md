
# Password Cracking Project

## 1. Problem Statement
This project explores and implements various password cracking and protection techniques. The focus is on understanding and demonstrating:

- Brute force attacks
- Dictionary attacks
- Rainbow tables
- Salted hashing

Additionally, the project includes protection mechanisms like rate limiting and password complexity checks to illustrate how passwords can be safeguarded against such attacks.

## 2. References
The project implements the following well-known password cracking methods:

- **Brute Force Attacks**: Attempts all possible password combinations.
- **Dictionary Attacks**: Uses wordlists such as `rockyou.txt` to guess passwords.
- **Rainbow Table Attacks**: Leverages precomputed hash values to speed up cracking.
- **Hashing Techniques**: Includes MD5, SHA-1, and SHA-256 to compare the performance of different hash algorithms.

## 3. Project Structure
The project consists of multiple scripts, each implementing a specific attack or protection mechanism:

### 3.1 Brute Force Attack (`brute_force_attack.py`)
**Description**: Generates all possible combinations of characters up to a certain length and compares them to the hashed password.
- **Example**: Successfully cracked the hash for the password `abc123`.

### 3.2 Dictionary Attack (`dictionary_attack.py`)
**Description**: Loads a wordlist and compares the hashed versions of the words to the target hash.
- **Example**: Cracked the password `12345678` using the wordlist.

### 3.3 Rainbow Table Attack (`rainbow_table_attack.py`)
**Description**: Precomputes hash values for a list of passwords and uses these to quickly find a matching password.
- **Example**: Found the password `abc123` using the rainbow table.

### 3.4 Hashing with Salt (`hashing_with_salt.py`)
**Description**: Uses a random salt to hash passwords, enhancing security by making it harder to crack passwords using precomputed tables.
- **Example**: The password `securepassword` was hashed with a random salt and successfully verified.

### 3.5 Password Complexity Check (`password_complexity_check.py`)
**Description**: Verifies whether a password meets certain security requirements (length, uppercase, lowercase, numbers, special characters).
- **Example**: The password `StrongPass1!` passed the security check.

### 3.6 Rate Limiting and CAPTCHA Simulation (`rate_limiting_and_captcha.py`)
**Description**: Limits failed login attempts and blocks further attempts after a set number of failures.
- **Example**: After five failed attempts, the user was temporarily blocked.

## 4. Running the Project
To run the project, execute the `main.py` file from the terminal:

```bash
./main.py
```

You will be presented with a menu to select and test different attacks or protection mechanisms:

1. Brute Force Attack
2. Dictionary Attack
3. Rainbow Table Attack
4. Hashing with Salt
5. Password Complexity Check
6. Rate Limiting and CAPTCHA Simulation

Follow the instructions on the screen after selecting an option.
