while True:
    topping = input("\nMasukkan topping pizza (atau ketik 'selesai'): ")
    if topping.lower() == 'selesai':
        break  # Langsung keluar dari loop saat ini juga
    else:
        print(f"-> Saya akan menambahkan {topping} ke pizza Anda!")

print("Selesai menambahkan topping. Terima kasih!")