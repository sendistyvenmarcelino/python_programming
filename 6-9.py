tempat_favorit = {
    'anto' : ['pantai kuta', 'gunung bromo', 'danau toba'],
    'andi' : ['candi borobudur', 'pulau komodo'],
    'tono' : ['gunung rinjani']
}
for nama, tempat in tempat_favorit.items():
    print(f"\nTempat favorit {nama.title()} adalah:")
    for t in tempat:
        print(f"- {t.title()}")