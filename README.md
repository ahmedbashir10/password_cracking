# Password Cracking and Protection Project

This project demonstrates various password-cracking techniques and protection mechanisms, including brute force, dictionary attacks, rainbow table attacks, and salted hashing. Additionally, protection mechanisms like password complexity checks are implemented to illustrate how to safeguard against these attacks

## Table of Contents
1. [Problem Statement](#problem-statement)
2. [References](#references)
3. [Project Structure](#project-structure)
4. [How to Use](#how-to-use)
5. [Examples and Results](#examples-and-results)
6. [Benchmarking](#benchmarking)

---

## Problem Statement

This project focuses on demonstrating the following techniques for password cracking:
- Brute Force Attacks
- Dictionary Attacks
- Rainbow Table Attacks
- Salted Hashing

In addition to these cracking techniques, the project includes:
- Password complexity checks to ensure strong password policies.

---

## References

The project utilizes and implements various hashing algorithms and password-cracking techniques, including:
- **MD5**
- **SHA-1**
- **SHA-224**
- **SHA-256**
- **SHA-512**
- **bcrypt**

References: 
- Read more about: 
    - hashlib [https://docs.python.org/3/library/hashlib.html] 
    - Geeksforgeeks [https://www.geeksforgeeks.org/understanding-rainbow-table-attack/]

---

## Project Structure

The project is organized into several Python scripts, each focusing on a specific password-cracking method or protection mechanism.

1. **Brute Force Attack** (`brute_force_attack.py`)
    - Tries all possible password combinations up to a specified length. It covers brute
    - Example: Cracked the password `abc123`.

2. **Dictionary Attack** (`dictionary_attack.py`)
    - Uses a wordlist of common passwords to attempt cracking.
    - Example: Found the password `password123`.

3. **Rainbow Table Attack** (`rainbow_table_attacks.py`)
    - Precomputes hash values for a list of passwords to speed up the cracking process.
    - Supports MD5, SHA-1, SHA-256, and other algorithms.
    - Example: Found the password `admin`.

4. **Hashing** (`hashing.py`)
    - Implements various hashing algorithms and supports salted hashing to demonstrate how salts can make password cracking harder.
    - Example: Successfully hashed and verified a password using bcrypt with salt.

5. **Password Complexity Check** (`password_complexity_check.py`)
    - Verifies that passwords meet a specified complexity (e.g., length, upper/lowercase letters, numbers, and symbols).
    - Example: Verified that the password `StrongPass123!` is secure.

6. **Benchmarking** (`benchmarkes.py`)
    - Compares the time it takes to crack passwords using different methods, including brute force, dictionary, and rainbow tables.
    - Example: Rainbow table attacks showed significantly reduced time compared to brute force attacks.

---

## How to Use

To run the project, follow these steps:

### 1. Clone the Repository

```bash
git clone <repository_url>
cd password_cracking
```

### 2. Install Dependencies
Make sure you have Python 3 installed. Then, install any required libraries:

```bash
pip install -r requirements.txt
```

### 3. Running the Main Program

To start the project and explore the different password-cracking methods and protection mechanisms, run the `main.py` script:

```bash
python main.py --terminal
```

You will be prompted to select which method or mechanism to test:

- **Brute Force Attack**
- **Dictionary Attack**
- **Rainbow Table Attack**
- **Hashing with Salt**
- **Password Complexity Check**

Simply choose the number for the desired attack or protection mechanism, and follow the on-screen instructions.

### 4. Running Benchmarks

To compare the efficiency of the different password-cracking methods, run the `benchmarkes.py` script:

```bash
python benchmarkes.py
```

This script will perform brute force, dictionary, and rainbow table attacks on the same password and display the time taken by each method.

---

## Examples and Results

### 1. Brute Force Attack Example

To run a brute force attack:

```bash
python main.py --terminal
# Select the "Brute Force Attack" option
# Enter the hash of the target password (e.g., SHA-256 hash of "password123")
```

The program will try all possible password combinations and show the time taken to find the correct password.

### 2. Dictionary Attack Example

To run a dictionary attack:

```bash
python main.py --terminal
# Select the "Dictionary Attack" option
# Provide a hash (e.g., MD5 hash of "password123") and the wordlist file
```

The program will compare the hashes of words in the wordlist to the target hash until it finds a match.

### 3. Rainbow Table Attack Example

To run a rainbow table attack:

```bash
python main.py --terminal
# Select the "Rainbow Table Attack" option
# Choose a hash algorithm (e.g., SHA-1) and provide the target hash
```

The rainbow table will be generated and saved for future use. Subsequent runs will load the table from disk, speeding up the attack.

---

## Benchmarking

The `benchmarkes.py` script compares the time taken by each method to crack a password. Here's an example of the results:

- **Brute Force (SHA-256)**: 2.345 seconds
- **Dictionary Attack (MD5)**: 0.456 seconds
- **Rainbow Table (SHA-1)**: 0.012 seconds (after table is saved)

To run the benchmarks:

```bash
python benchmarkes.py
```

You will be prompted to provide a password, maximum length, and hash algorithm, and the script will display a bar graph comparing the times.

---

### Additional Tips:
1. **Wordlists**: For the dictionary attack, you can use common wordlists like `rockyou.txt`. You can also create your own.
2. **Hash Algorithms**: You can choose different hashing algorithms (e.g., MD5, SHA-1, SHA-256) for both brute force and rainbow table attacks to compare their performance.
3. **Salting**: For added protection, salting your passwords significantly increases the difficulty of cracking, as demonstrated in the salted hashing feature.

---

### Contributions:
- Adam worked on developing brute force attacks and dictionary attacks. He also started implementing these along with the main file. Additionally, he contributed to hashing algorithms such as MD5 and SHA-256. Lastly, he has contributed to the password-checking mechanics and the presentation slides. 
Ahmed implemented the rainbow table attack and different hashing algorithms, such as bcrypt, SHA-1, and SHA-224. He also worked on benchmarking and, together with Adam, helped with the password-checking mechanics and the presentation slides.
