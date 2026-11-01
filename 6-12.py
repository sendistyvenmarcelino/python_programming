kota_kota = {
    'jakarta': {
        'negara': 'Indonesia',
        'populasi': '10.5 juta',
        'fakta': 'Kota dengan sistem transportasi bus rapid transit (BRT) terpanjang di dunia.',
        'wisata': 'Monumen Nasional (Monas), Kota Tua, Ancol, dan Taman Mini Indonesia Indah.'
    },
    'tokyo': {
        'negara': 'Jepang',
        'populasi': '37.4 juta',
        'fakta': 'Merupakan wilayah metropolitan terpadat di dunia.',
        'wisata': 'Kuil Senso-ji, Menara Tokyo, Shibuya Crossing, dan Istana Kekaisaran.'
    },
    'paris': {
        'negara': 'Prancis',
        'populasi': '2.1 juta',
        'fakta': 'Terkenal dengan julukan "City of Light" atau Kota Cahaya.',
        'wisata': 'Menara Eiffel, Museum Louvre, Katedral Notre-Dame, dan Sungai Seine.'
    }
}
print("=" * 50)
print("Informasi tentang beberapa kota di dunia:")
print("=" * 50)
for nama_kota, info_kota in kota_kota.items():
    print(f"\nKota: {nama_kota.title()}")
    print(f"  negara   : {info_kota['negara']}")
    print(f"  populasi : {info_kota['populasi']}")
    print(f"  fakta    : {info_kota['fakta']}")
    print(f"  wisata   : {info_kota['wisata']}")
    print("-" * 50)