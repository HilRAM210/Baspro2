status_list = ["Tetap", "Honor"]
golongan_list = ["A", "B", "C"]

print("\n\t\t\t\t\tDAFTAR GAJI\n")

for status in status_list:
    for golongan in golongan_list:
        gaji = 0
        bonus = 0

        if status == "Tetap":
            gaji = 1000000
        elif status == "Honor":
            gaji = 750000

        if golongan == "A":
            bonus = 200000 if status == "Tetap" else 150000
        elif golongan == "B":
            bonus = 400000 if status == "Tetap" else 275000
        elif golongan == "C":
            bonus = 550000 if status == "Tetap" else 480000

        total_gaji = gaji + bonus

        print("| Status |", status, "| Golongan |", golongan, "| Gaji |", gaji, "| Bonus |", bonus, "| Total Gaji |", total_gaji, " |")