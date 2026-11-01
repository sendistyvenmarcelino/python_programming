angka_favorit = {
    'doni' : [7, 14, 28],
    'toni' : [5, 10],
    'lina' : [9, 99, 999]
}
for nama, angka in angka_favorit.items():
    print(f"\nAngka favorit {nama.title()} adalah:")
    for a in angka:
        print(f"- {a}")