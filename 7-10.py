hasil_survei = {}
survei_aktif = True
while survei_aktif:
    nama = input("\nsiapa nama Anda? ")
    jawaban = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda ingin pergi? ")
    hasil_survei[nama] = jawaban
    ulangi = input("Apakah ada orang lain yang ingin mengisi survei? (ya/tidak) ")
    if ulangi.lower() == 'tidak':
        survei_aktif = False
print("\n--- Hasil Survei Liburan Impian ---")
for nama, tempat in hasil_survei.items():
    print(f"{nama.title()} ingin liburan ke {tempat.title()}.")