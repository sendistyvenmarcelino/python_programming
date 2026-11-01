kamus = {
    'variable': 'Wadah untuk menyimpan nilai data.',
    'list': 'Koleksi item yang berurutan dan dapat diubah.',
    'dictionary': 'Koleksi pasangan kunci-nilai (key-value pairs).',
    'loop': 'Instruksi untuk mengulang blok kode tertentu.',
    'string': 'Deretan karakter atau teks.',
    'comment' : 'Catatan dalam kode yang diabaikan oleh komputer.',
    'boolean' : 'Tipe data yang bernilai True atau False.',
    'float' : 'Angka desimal.',
    'function' : 'Blok kode yang hanya berjalan saat dipanggil.',
    'syntax' : 'Aturan struktur penulisan kode.'
}
for kata, definisi in kamus.items():
    print(f"{kata.title()}: {definisi}")