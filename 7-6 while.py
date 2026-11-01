topping = ""
while topping != 'selesai':
    topping = input("\nMasukkan topping pizza (atau ketik 'selesai'): ")
    
    if topping != 'selesai':
        print(f"-> Saya akan menambahkan {topping} ke pizza Anda!")

print("Selesai menambahkan topping. Terima kasih!")