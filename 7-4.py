while True:
    topping = input("\nMasukkan topping pizza (atau ketik 'selesai'): ")
    
    if topping.lower() == 'selesai':
        print("Selesai menambahkan topping. Terima kasih!")
        break
    else:
        print(f"-> Saya akan menambahkan {topping} ke pizza Anda!")