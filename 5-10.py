user_lama = ['budi', 'susi', 'john', 'andi', 'lina']
user_baru = ['JOHN', 'budi', 'lina', 'alex', 'messi']
user_lama_lower = [user.lower() for user in user_lama]
for userb in user_baru:
    if userb.lower() in user_lama_lower:
        print(f"maaf, nama '{userb}' sudah digunakan. Silahkan pilih nama lain.")
    else:
        print(f"selamat, nama '{userb}' tersedia.")