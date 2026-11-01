def buat_album(nama_musisi, judul_album, jumlah_lagu=None):
    data_album = {
        'musisi': nama_musisi,
        'judul': judul_album
    }
    if jumlah_lagu:
        data_album['jumlah_lagu'] = jumlah_lagu
    return data_album
album_1 = buat_album("payung teduh", "Dunia Batas")
album_2 = buat_album("Oasis", '(What’s the Story) Morning Glory?')
album_3 = buat_album("The Jeblogs", "Sambutlah", jumlah_lagu=8)
print(album_1)
print(album_2)
print(album_3)