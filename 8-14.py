def buat_mobil(pabrikan, model, **info_mobil):
    info_mobil['pabrikan'] = pabrikan
    info_mobil['model'] = model
    return info_mobil
mobil = buat_mobil('ferrari', 'testa rossa', warna='merah', tahun=2022, transmisi='manual')
print(mobil)