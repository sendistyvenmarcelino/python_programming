daftar_pesan = [
    "Apa Kabarmu?",
    "jangan telat makan ya.",
    "Besok ada kelas pagi woi"
]
pesan_terkirim = []
def kirim_pesan(pesan_belum_terkirim, pesan_sudah_terkirim):
    while pesan_belum_terkirim:
        pesan = pesan_belum_terkirim.pop(0)
        print(f"Mengirim pesan: {pesan}")
        pesan_sudah_terkirim.append(pesan)
kirim_pesan(daftar_pesan[:], pesan_terkirim)
print("\n--- Verifikasi Daftar ---")
print(f"Daftar pesan asli (tetap utuh/ada isi): {daftar_pesan}")
print(f"Daftar pesan terkirim: {pesan_terkirim}")