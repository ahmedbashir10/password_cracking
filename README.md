README: Password Cracking Project
1. Problem Statement
This project aims to explore and implement different techniques for password cracking and protection, including brute force attacks, dictionary attacks, rainbow tables, and salted hashing. We also include protection mechanisms like rate limiting and password complexity checks. The goal is to understand how these attacks work and how to protect passwords from such threats.

2. References
The project uses well-known password cracking methods, including:

Brute force attacks to guess all possible password combinations.
Dictionary attacks using the "rockyou.txt" wordlist.
Rainbow table attacks to speed up password cracking by using precomputed hash values.
Hashing techniques like MD5, SHA-1, and SHA-256 were used to compare the performance of different hash algorithms.
3. Project Documentation
The project is divided into several parts, each implementing different password cracking and protection techniques. Here's a quick overview:

3.1 
Brute Force Attack (brute_force_attack.py)
Description: This script generates all possible combinations of characters up to a certain length and compares them to the hashed password.
Example: The hash for the password "abc123" was successfully cracked.

3.2
Dictionary Attack (dictionary_attack.py)
Description: The dictionary attack loads a wordlist and compares the hashed versions of the words to the hash you want to crack.
Example: The script cracked the password "12345678" using the wordlist.

3.3
Rainbow Table Attack (rainbow_table_attack.py)
Description: This script precomputes hash values for a list of passwords and uses these to quickly find a matching password.
Example: The password "abc123" was found using the rainbow table.

3.4
Hashing with Salt (hashing_with_salt.py)
Description: This script uses a random salt to hash passwords, which increases security and makes it harder to crack passwords using rainbow tables.
Example: The password "securepassword" was hashed with a random salt and verified.

3.5 
Password Complexity Check (password_complexity_check.py)
Description: This checks if a password meets specific security requirements, such as length, uppercase letters, lowercase letters, numbers, and special characters.
Example: The password "StrongPass1!" was approved as a secure password.

3.6 
Rate Limiting and CAPTCHA Simulation (rate_limiting_and_captcha.py)
Description: This limits the number of failed login attempts and blocks further attempts after a set number of failures.
Example: After five failed attempts, the user was temporarily blocked.


4. Running the Project
You can run the main menu by executing main.py directly from the terminal:
./main.py

You will see a menu where you can choose which attack or protection mechanism to test:

1. Brute Force Attack
2. Dictionary Attack
3. Rainbow Table Attack
4. Hashing with Salt
5. Password Complexity Check
6. Rate Limiting and CAPTCHA Simulation
Enter the number for the attack or protection mechanism you want to test, and follow the instructions on the screen.

