aktif = True
while aktif:
    topping = input("\nMasukkan topping pizza (atau ketik 'selesai'): ")
    if topping.lower() == 'selesai':
        aktif = False 
    else:
        print(f"-> Saya akan menambahkan {topping} ke pizza Anda!")
print("Selesai menambahkan topping. Terima kasih!")