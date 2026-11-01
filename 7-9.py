pesanan_sandwich = ['pastrami', 'keju', 'telur', 'pastrami', 'selada', 'pastrami', 'tomat']
sandwich_selesai = []
print("Maaf, toko kami kehabisan pastrami hari ini.")
while 'pastrami' in pesanan_sandwich:
    pesanan_sandwich.remove('pastrami')
while pesanan_sandwich:
    sandwich_sekarang = pesanan_sandwich.pop(0)
    print(f"Saya sedang membuat sandwich {sandwich_sekarang}.")
    sandwich_selesai.append(sandwich_sekarang)
print("\nSemua sandwich telah selesai dibuat:")
for sandwich in sandwich_selesai:
    print(f"- Sandwich {sandwich}")