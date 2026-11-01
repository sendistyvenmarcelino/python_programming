prompt = "\nBerapa usia anda?"
prompt += "\n(Ketik 'quit' untuk keluar): "
while True:
    usia = input(prompt)
    if usia == 'quit':
        break
    usia = int(usia)
    if usia < 3:
        print("Tiket gratis.")
    elif usia < 13:
        print("Tiket anak-anak: $10.")
    else:
        print("Tiket dewasa: $15.")