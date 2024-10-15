import matplotlib.pyplot as plt
from attacks import rainbow_table_attacks
from attacks.brute_force import *
from attacks.brute_force_attack import brute_force_hashed_with_salt, brute_force_hashed_no_salt, brute_force_plaintext, optimized_brute_force_hashed
from attacks.dictionary_attack import dictionary_attack
from attacks.rainbow_table_attack import rainbow_table_attack
from attacks.rainbow_table_attacks import generate_rainbow_table
from utils.hashing import hash_password, hash_password_with_salt
from utils.password_complexity_check import check_password_strength



def benchmark_attacks(target_password, salt, max_length, hash_algo):
    # Hash the target password using the provided algorithm
    target_hash = hash_password(target_password, hash_algo)
    
    # Initialize a dictionary to store time taken by each attack
    benchmark_results = {}

    # 1. Plaintext Brute Force (No Hash)
    start_time = time.time()
    brute_force_plaintext(target_password, max_length)
    benchmark_results['Brute Force (Plaintext)'] = time.time() - start_time

    # 2. Brute Force with No Salt
    start_time = time.time()
    brute_force_hashed_no_salt(target_hash, max_length, hash_algo)
    benchmark_results['Brute Force (Hashed, No Salt)'] = time.time() - start_time

    # 3. Brute Force with Salt
    start_time = time.time()
    brute_force_hashed_with_salt(target_hash, salt, max_length, hash_algo)
    benchmark_results['Brute Force (Hashed with Salt)'] = time.time() - start_time

    # 4. Optimized Brute Force
    start_time = time.time()
    optimized_brute_force_hashed(target_hash, max_length, hash_algo)
    benchmark_results['Brute Force (Optimized)'] = time.time() - start_time

    # 5. Dictionary Attack
    start_time = time.time()
    dictionary_attack(target_hash)
    benchmark_results['Dictionary Attack'] = time.time() - start_time

    # 6. Rainbow Table Attack
    rainbow_table = generate_rainbow_table(hash_algo)  # Generate rainbow table
    start_time = time.time()
    rainbow_table_attacks(target_hash, rainbow_table)
    benchmark_results['Rainbow Table Attack'] = time.time() - start_time

    # Return the benchmark results
    return benchmark_results


# Visualization function
def plot_benchmark_results(results):
    # Extract attack names and times
    attack_names = list(results.keys())
    times = list(results.values())

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(attack_names, times, color='skyblue')
    plt.xlabel('Time Taken (seconds)')
    plt.ylabel('Attack Method')
    plt.title('Benchmark Results: Password Cracking Methods')
    plt.show()

def run_benchmark():
    target_password = input("Enter the target password for benchmarking: ")
    #salt = input("Enter the salt value to use: ")
    max_length = int(input("Enter the maximum password length for brute force: "))
    hash_algo = input("Enter the hashing algorithm (e.g., sha256, bcrypt): ")

    # Run the benchmark
    benchmark_results = benchmark_attacks(target_password, 0, max_length, hash_algo)

    # Plot the results
    plot_benchmark_results(benchmark_results)


if __name__ == "__main__":
    run_benchmark()