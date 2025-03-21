import math
import os
import msvcrt

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def getch():
    if os.name == 'nt':
        return msvcrt.getch().decode('utf-8')
    else:
        import getch
        return getch.getch()

def luas_segitiga():
    print("\nMenghitung Luas Segitiga")
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * alas * tinggi
    print(f"Luas segitiga adalah: {luas}\n")
    getch()
    clear_screen()

def luas_lingkaran():
    print("\nMenghitung Luas Lingkaran")
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    luas = math.pi * jari_jari ** 2
    print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas}")
    getch()
    clear_screen()

def luas_tabung():
    print("\nMenghitung Volume Tabung")
    jari_jari = float(input("Masukkan jari-jari alas tabung: "))
    tinggi = float(input("Masukkan tinggi tabung: "))
    volume = math.pi * jari_jari ** 2 * tinggi
    print(f"Volume tabung dengan jari-jari {jari_jari} dan tinggi {tinggi} adalah {volume}")
    getch()
    clear_screen()

def tampilkan_menu():
    print("=== Program Menghitung Luas ===")
    print("1. Luas Segitiga")
    print("2. Luas Lingkaran")
    print("3. Volume Tabung")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")
    return pilihan

def main():
    while True:
        pilihan = tampilkan_menu()
        if pilihan == '1':
            luas_segitiga()
        elif pilihan == '2':
            luas_lingkaran()
        elif pilihan == '3':
            luas_tabung()
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")
            getch()
            clear_screen()

main()