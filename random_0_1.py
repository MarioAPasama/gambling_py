import random

def generate_random_binary():
    return random.randint(0, 1)

# Contoh penggunaan
if __name__ == "__main__":
    for _ in range(10):  # Menghasilkan 10 angka acak 0 atau 1
        print(generate_random_binary())
