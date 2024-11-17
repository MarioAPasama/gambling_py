import random

def generate_random_binary():
    return random.randint(0, 1)

# Contoh penggunaan
if __name__ == "__main__":
    init_value = 1
    incorrectly = 6
    consecutive_fails = 0

    for i in range(1, 101):  # Iterasi hingga 100 kali sebagai batas maksimal
        print(f"Iterasi ke-{i}:")
        binary_value = generate_random_binary()
        is_correct = binary_value == init_value
        print(f"Nilai random: {binary_value}")
        print(f"Apakah sama dengan init_value ({init_value}): {is_correct}")

        if not is_correct:
            consecutive_fails += 1
        else:
            consecutive_fails = 0  # Reset jika kembali ke True
        
        if consecutive_fails >= incorrectly:
            print(f"\nTelah terjadi {incorrectly} kesalahan berturut-turut. Program dihentikan.")
            break
        print(f"Kesalahan berturut-turut saat ini: {consecutive_fails}\n")
