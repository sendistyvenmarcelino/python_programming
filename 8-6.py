def kota_negara(kota, negara):
    return f"{kota.title()}, {negara.title()}"
tempat1 = kota_negara("jakarta", "indonesia")
tempat2 = kota_negara("milan", "italia")
tempat3 = kota_negara("edinburgh", "skotlandia")
print(tempat1)
print(tempat2)
print(tempat3)
