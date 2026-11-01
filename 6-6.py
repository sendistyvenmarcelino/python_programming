bahasa_favorit = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
daftar_peserta = ['jen', 'budi', 'phil', 'siti', 'ryan']
for nama in daftar_peserta:
    if nama in bahasa_favorit.keys():
        print(f"Terima kasih {nama.title()} karena sudah bersedia mengisi polling!")
    else:
        print(f"Halo {nama.title()}, kami mengundang Anda untuk mengikuti polling bahasa favorit kami.")