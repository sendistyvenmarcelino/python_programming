def bangun_profil(nama_depan, nama_belakang, **info_tambahan):
    profil = {}
    profil['nama_depan'] = nama_depan
    profil['nama_belakang'] = nama_belakang
    for kunci, nilai in info_tambahan.items():
        profil[kunci] = nilai
    return profil
profil_saya = bangun_profil(
    'Stephen',
    'James',
    lokasi='Sukoharjo',
    pekerjaan='Pelajar',
    hobi='mancing'
)
print(profil_saya)