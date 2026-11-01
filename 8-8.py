def buat_album(nama_musisi, judul_album):
    data_album = {
        'musisi': nama_musisi,
        'judul': judul_album
    }
    return data_album
while True:
    print("\n--- Masukkan Infrormasi Album ---")
    print("(Ketik 'q' untuk keluar)")
    musisi = input("Nama Musisi: ")
    if musisi.lower() == 'q':
        break
    judul = input("Judul Album: ")
    if judul.lower() == 'q':
        break   
    album_pengguna = buat_album(musisi, judul)
    print("\nAlbum yang berhasil dibuat:")
    print(album_pengguna)
print("\nTerima kasih telah menggunakan program ini!")