def buat_sandwich(*bahan_bahan):
    print("\nMembuat sandwich dengan bahan-bahan berikut:")
    for bahan in bahan_bahan:
        print(f"- {bahan}")
buat_sandwich('tuna', 'selada', 'tomat')
buat_sandwich('daging', 'keju', 'telur')
buat_sandwich('selai kacang', 'pisang', 'madu')
