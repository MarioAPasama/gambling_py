import random

def random_murni_with_validation(max_fails):
    """
    Menghasilkan nilai random murni dan memvalidasi dengan aturan reset toleransi.
    """
    init_value = 1  # Nilai awal yang ingin dicek
    consecutive_fails = 0  # Jumlah kesalahan berturut-turut

    for i in range(1, 101):  # Iterasi hingga 100 kali sebagai batas
        # Generate nilai random secara murni
        random_value = random.randint(0, 1)
        print(f"Iterasi ke-{i}: Nilai random: {random_value}, Init value: {init_value}")

        # Validasi nilai random terhadap init_value
        if random_value == init_value:
            print(f"Benar! Reset kesalahan berturut-turut.")
            consecutive_fails = 0  # Reset kesalahan berturut-turut
        else:
            consecutive_fails += 1
            print(f"Salah! Kesalahan berturut-turut: {consecutive_fails}")

        # Jika kesalahan berturut-turut mencapai batas, hentikan program
        if consecutive_fails >= max_fails:
            print(f"\nTelah terjadi {max_fails} kesalahan berturut-turut. Program dihentikan.")
            break

        # Ganti nilai init_value untuk iterasi berikutnya (bergantian 0 dan 1)
        init_value = 1 if init_value == 0 else 0

    print("\nProgram selesai.")

# Contoh penggunaan
if __name__ == "__main__":
    random_murni_with_validation(max_fails=6)
