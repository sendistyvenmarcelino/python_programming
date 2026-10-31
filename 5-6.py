usia = 42 # ini bisa diubah untuk menguji kategori usia lainnya

if usia < 2:
    print("Orang ini adalah bayi (baby).")
elif usia < 4:
    print("Orang ini adalah balita (toddler).")
elif usia < 13:
    print("Orang ini adalah anak-anak (kid).")
elif usia < 20:
    print("Orang ini adalah remaja (teenager).")
elif usia < 65:
    print("Orang ini adalah orang dewasa (adult).")
else:
    print("Orang ini adalah lansia (elder).")