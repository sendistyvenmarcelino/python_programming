hewan_1 = {'jenis' : 'kucing', 'pemilik' : 'budi'}
hewan_2 = {'jenis' : 'anjing', 'pemilik' : 'susi'}
hewan_3 = {'jenis' : 'burung', 'pemilik' : 'andi'}
hewan_peliharaan = [hewan_1, hewan_2, hewan_3]
for hewan in hewan_peliharaan:
    print(f"\nJenis hewan: {hewan['jenis'].title()}")
    print(f"Pemilik: {hewan['pemilik'].title()}")