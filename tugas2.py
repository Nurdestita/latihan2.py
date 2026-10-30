import math
print("=== MEMU PILIHAN LINGKARAN ===")   
print("1. Menghitung Keliling Lingkaran") 
print("2. Menghitung Luas Lingkaran")

pilihan = input("Masukan pilihan Anda (1 atau 2): ")
if pilihan == "1" or pilihan == "2":
    jari_jari = float(input("Masukan nilai jari-jari (r): "))

    if pilihan == "1":
        keliling = 2 * math.pi * jari_jari
        print(f"Keliling lingkaran dengan jari-jari {jari_jari} adalah: {keliling:.2f}")
    elif pilihan == "2":
        luas = math.pi * (jari_jari ** 2)
        print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah: {luas:.2f}")
else:
    print("Pilihan tidak valid! Silakan jalankan ulang dan pilih angka 1 atau 2.")
            