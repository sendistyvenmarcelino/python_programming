kamus = {
    'variable': 'Wadah untuk menyimpan nilai data.',
    'list': 'Koleksi item yang berurutan dan dapat diubah.',
    'dictionary': 'Koleksi pasangan kunci-nilai (key-value pairs).',
    'loop': 'Instruksi untuk mengulang blok kode tertentu.',
    'string': 'Deretan karakter atau teks.'
}

# Mencetak dengan format rapi
for kata, definisi in kamus.items():
    print(f"{kata.title()}:\n\t{definisi}\n")