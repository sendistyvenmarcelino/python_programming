pesanan_sandwich = ['tuna', 'ayam', 'daging sapi', 'keju', 'telur']
sandwich_selesai = []
while pesanan_sandwich:
    sandwich_sekarang = pesanan_sandwich.pop(0)
    print(f"Saya sedang membuat sandwich {sandwich_sekarang}.")
    sandwich_selesai.append(sandwich_sekarang)
print("\nSemua sandwich telah selesai dibuat:")
for sandwich in sandwich_selesai:
    print(f"- Sandwich {sandwich}")