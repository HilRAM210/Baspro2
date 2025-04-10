nama = input("Input Nama: ")
nik = input("Input NIK: ")
status = input("Input Status (Tetap/Honor): ")
golongan = input("Input Golongan (A/B/C): ")

gaji = 0
bonus = 0

if status == "Tetap" or status == "tetap" or status == "TETAP":
    gaji = 1000000
    if golongan == "A" or golongan == "a":
        bonus = 200000
    elif golongan == "B" or golongan == "b":
        bonus = 400000
    elif golongan == "C" or golongan == "c":
        bonus = 550000
    else:
        print("Golongan Tidak Valid !!!")
        exit()
elif status == "Honor" or status == "honor" or status == "HONOR":
    gaji = 750000
    if golongan == "A" or golongan == "a":
        bonus = 150000
    elif golongan == "B" or golongan == "b":
        bonus = 275000
    elif golongan == "C" or golongan == "c":
        bonus = 480000
    else:
        print("Golongan Tidak Valid !!!")
        exit()
else:
    print("Status Tidak Valid !!!")
    exit()

total_gaji = gaji + bonus

print("\n=== Struk Gaji ===")
print("Nama:", nama)
print("NIK:", nik)
print("Status:", status)
print("Golongan:", golongan)
print("Gaji:", gaji)
print("Bonus:", bonus)
print("Total", total_gaji)
