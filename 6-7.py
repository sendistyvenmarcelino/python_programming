orang_1 = {
    'nama_depan': 'Budi',
    'nama_belakang': 'Santoso',
    'usia': 25,
    'kota': 'Jakarta'
}
orang_2 = {
    'nama_depan': 'Siti',
    'nama_belakang': 'Aminah',
    'usia': 22,
    'kota': 'Bandung'
}
orang_3 = {
    'nama_depan': 'Joko',
    'nama_belakang': 'Susilo',
    'usia': 30,
    'kota': 'Surabaya'
}
orang_orang = [orang_1, orang_2, orang_3]
for orang in orang_orang:
    nama_lengkap = f"{orang['nama_depan']} {orang['nama_belakang']}"
    print(f"\nNama Lengkap: {nama_lengkap}")
    print(f"Usia        : {orang['usia']} tahun")
    print(f"Kota Tinggal: {orang['kota']}")