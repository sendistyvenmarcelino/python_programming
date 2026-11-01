angka = input("masukkan satu angka, dan saya akan beri tahu apakah itu kelipatan 10: ")
angka = int(angka)
if angka % 10 == 0:
    print(f"{angka} adalah kelipatan 10.")
else:
    print(f"{angka} bukan kelipatan 10.")