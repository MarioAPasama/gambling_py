# import random

# def random_murni_with_history(max_fails):
#     """
#     Menghasilkan nilai random murni dengan riwayat untuk membaca pola.
#     """
#     init_value = 1  # Nilai awal yang ingin dicek
#     consecutive_fails = 0  # Jumlah kesalahan berturut-turut
#     history = []  # Menyimpan riwayat hasil random

#     for i in range(1, 101):  # Iterasi hingga 100 kali sebagai batas
#         # Generate nilai random secara murni
#         random_value = random.randint(0, 1)
#         history.append(random_value)  # Simpan ke riwayat
#         print(f"Iterasi ke-{i}: Nilai random: {random_value}, Init value: {init_value}")

#         # Validasi nilai random terhadap init_value
#         if random_value == init_value:
#             print(f"Benar! Reset kesalahan berturut-turut.")
#             consecutive_fails = 0  # Reset kesalahan berturut-turut
#         else:
#             consecutive_fails += 1
#             print(f"Salah! Kesalahan berturut-turut: {consecutive_fails}")

#         # Jika kesalahan berturut-turut mencapai batas, hentikan program
#         if consecutive_fails >= max_fails:
#             print(f"\nTelah terjadi {max_fails} kesalahan berturut-turut. Program dihentikan.")
#             break

#         # Ganti nilai init_value untuk iterasi berikutnya (bergantian 0 dan 1)
#         init_value = 1 if init_value == 0 else 0

#     # Analisis pola dari riwayat
#     print("\nRiwayat Hasil Random:")
#     print(history)
#     print(f"Distribusi: 0 -> {history.count(0)}, 1 -> {history.count(1)}")
#     print("\nProgram selesai.")

# # Contoh penggunaan
# if __name__ == "__main__":
#     random_murni_with_history(max_fails=10)

# import random
# import matplotlib.pyplot as plt

# def random_murni(max_fails):
#     """
#     Algoritma terbaik untuk random murni dengan riwayat, analisis pola, dan visualisasi.
#     """
#     init_value = 1  # Nilai awal yang ingin dicek
#     consecutive_fails = 0  # Kesalahan berturut-turut
#     history = []  # Riwayat nilai random

#     for i in range(1, 1440):  # Iterasi hingga 100 kali
#         # Generate nilai random secara murni
#         random_value = random.randint(0, 1)
#         history.append(random_value)

#         # Validasi nilai random terhadap init_value
#         if random_value == init_value:
#             consecutive_fails = 0  # Reset kesalahan jika benar
#         else:
#             consecutive_fails += 1

#         # Jika kesalahan berturut-turut mencapai batas, hentikan program
#         if consecutive_fails >= max_fails:
#             print(f"\nTelah terjadi {max_fails} kesalahan berturut-turut. Program dihentikan.")
#             break

#         # Ganti nilai init_value secara bergantian
#         init_value = 1 if init_value == 0 else 0

#     # Analisis dan visualisasi
#     analyze_and_visualize(history, max_fails)

# def analyze_and_visualize(history, max_fails):
#     """
#     Analisis pola dari riwayat dan visualisasi hasil random.
#     """
#     # Distribusi hasil
#     count_0 = history.count(0)
#     count_1 = history.count(1)

#     print("\nAnalisis Riwayat:")
#     print(f"Total Iterasi: {len(history)}")
#     print(f"Distribusi: 0 -> {count_0}, 1 -> {count_1}")

#     # Analisis maksimum kesalahan berturut-turut
#     max_fails_found = analyze_consecutive_fails(history)
#     print(f"Maksimum kesalahan berturut-turut yang tercatat: {max_fails_found}")

#     # Visualisasi hasil random
#     visualize_results(history, max_fails)

# def analyze_consecutive_fails(history):
#     """
#     Analisis jumlah kesalahan berturut-turut maksimum dari riwayat.
#     """
#     max_fails = 0
#     current_fails = 0

#     init_value = 1  # Nilai awal untuk analisis
#     for value in history:
#         if value != init_value:
#             current_fails += 1
#             max_fails = max(max_fails, current_fails)
#         else:
#             current_fails = 0
#         init_value = 1 if init_value == 0 else 0  # Bergantian

#     return max_fails

# def visualize_results(history, max_fails):
#     """
#     Visualisasi pola dan distribusi hasil random.
#     """
#     plt.figure(figsize=(12, 6))

#     # Plot pola hasil random
#     plt.subplot(1, 2, 1)
#     plt.plot(history, marker='o', linestyle='-', label='Random Value')
#     plt.title('Pola Hasil Random')
#     plt.xlabel('Iterasi')
#     plt.ylabel('Nilai Random')
#     plt.yticks([0, 1])
#     plt.grid(True)
#     plt.legend()

#     # Plot distribusi hasil
#     plt.subplot(1, 2, 2)
#     plt.hist(history, bins=2, edgecolor='black', rwidth=0.8)
#     plt.title('Distribusi Hasil Random')
#     plt.xlabel('Nilai Random')
#     plt.ylabel('Frekuensi')
#     plt.xticks([0, 1])

#     # Tampilkan
#     plt.tight_layout()
#     plt.show()

# # Contoh penggunaan
# if __name__ == "__main__":
#     random_murni(max_fails=10)

import random
import matplotlib.pyplot as plt

def random_murni_with_data_collection(initial_data_count, max_fails, total_iterations):
    """
    Program yang mengumpulkan data random terlebih dahulu sebelum memvalidasi kesalahan berturut-turut.
    """
    if initial_data_count >= total_iterations:
        raise ValueError("initial_data_count harus lebih kecil dari total_iterations untuk menyisakan iterasi validasi.")

    init_value = 1  # Nilai awal yang ingin dicek
    consecutive_fails = 0  # Kesalahan berturut-turut
    history = []  # Menyimpan riwayat hasil random

    # Tahap 1: Pengumpulan data
    print(f"--- Tahap Pengumpulan Data ({initial_data_count} iterasi) ---")
    for i in range(1, initial_data_count + 1):
        random_value = random.randint(0, 1)
        history.append(random_value)
        print(f"Iterasi ke-{i}: Nilai random: {random_value}")

    # Analisis awal distribusi
    print("\nAnalisis Awal Distribusi:")
    print(f"0 -> {history.count(0)}, 1 -> {history.count(1)}")

    # Tahap 2: Memulai validasi dengan max_fails
    print(f"\n--- Tahap Validasi dengan Max Fails ({max_fails}) ---")
    for i in range(initial_data_count + 1, total_iterations + 1):
        random_value = random.randint(0, 1)
        history.append(random_value)
        print(f"Iterasi ke-{i}: Nilai random: {random_value}, Init value: {init_value}")

        # Validasi nilai random terhadap init_value
        if random_value == init_value:
            consecutive_fails = 0  # Reset kesalahan jika benar
            print(f"Benar! Reset kesalahan berturut-turut.")
        else:
            consecutive_fails += 1
            print(f"Salah! Kesalahan berturut-turut: {consecutive_fails}")

        # Jika kesalahan berturut-turut mencapai batas, hentikan program
        if consecutive_fails >= max_fails:
            print(f"\nTelah terjadi {max_fails} kesalahan berturut-turut. Program dihentikan.")
            break

        # Ganti nilai init_value secara bergantian
        init_value = 1 if init_value == 0 else 0

    # Analisis dan visualisasi
    analyze_and_visualize(history)

def analyze_and_visualize(history):
    """
    Analisis pola dari riwayat dan visualisasi hasil random.
    """
    # Distribusi hasil
    count_0 = history.count(0)
    count_1 = history.count(1)

    print("\nAnalisis Akhir Riwayat:")
    print(f"Total Iterasi: {len(history)}")
    print(f"Distribusi: 0 -> {count_0}, 1 -> {count_1}")

    # Visualisasi hasil random
    visualize_results(history)

def visualize_results(history):
    """
    Visualisasi pola dan distribusi hasil random.
    """
    plt.figure(figsize=(12, 6))

    # Plot pola hasil random
    plt.subplot(1, 2, 1)
    plt.plot(history, marker='o', linestyle='-', label='Random Value')
    plt.title('Pola Hasil Random')
    plt.xlabel('Iterasi')
    plt.ylabel('Nilai Random')
    plt.yticks([0, 1])
    plt.grid(True)
    plt.legend()

    # Plot distribusi hasil
    plt.subplot(1, 2, 2)
    plt.hist(history, bins=2, edgecolor='black', rwidth=0.8)
    plt.title('Distribusi Hasil Random')
    plt.xlabel('Nilai Random')
    plt.ylabel('Frekuensi')
    plt.xticks([0, 1])

    # Tampilkan
    plt.tight_layout()
    plt.show()

# Contoh penggunaan
if __name__ == "__main__":
    # total_iterations mencakup pengumpulan data dan validasi
    random_murni_with_data_collection(initial_data_count=2880, max_fails=10, total_iterations=10000)
