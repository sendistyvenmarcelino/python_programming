while True:
    topping = input("\nMasukkan topping pizza (atau ketik 'selesai'): ")
    if topping.lower() == 'selesai':
        break
    else:
        print(f"-> Saya akan menambahkan {topping} ke pizza Anda!")
print("Selesai menambahkan topping. Terima kasih!")