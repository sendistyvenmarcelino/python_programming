from numpy import rint


tamu = ["Cristiano Ronaldo", "Lionel Messi", "Jesse Lingard"]
print("--- Daftar Tamu Undangan Makan Malam ---")
print(f"Halo {tamu[0]}, saya mengundang Anda untuk makan malam di rumah saya.")
print(f"Halo {tamu[1]}, saya mengundang Anda untuk makan malam di rumah saya.")
print(f"Halo {tamu[2]}, saya mengundang Anda untuk makan malam di rumah saya.")
print("Halo semua, saya menemukan meja makan yang lebih besar nih")
tamu.insert(0, "Neymar Jr")
tamu.insert(1, "Kylian Mbappe")
tamu.append("Erling Haaland")
print("--- Daftar Tamu Undangan Makan Malam Terbaru ---")
for t in tamu:
    print(f"Halo {t}, saya mengundang Anda untuk makan malam di rumah saya.")
print("Maaf teman-teman, saya hanya bisa mengundang dua orang saja untuk makan malam.")
tamu_dihapus = tamu.pop()
print(f"Maaf {tamu_dihapus}, saya tidak bisa mengundang Anda untuk makan malam.")
tamu_dihapus = tamu.pop()
print(f"Maaf {tamu_dihapus}, saya tidak bisa mengundang Anda untuk makan malam.")
tamu_dihapus = tamu.pop()
print(f"Maaf {tamu_dihapus}, saya tidak bisa mengundang Anda untuk makan malam.")
tamu_dihapus = tamu.pop()
print(f"Maaf {tamu_dihapus}, saya tidak bisa mengundang Anda untuk makan malam.")
print("--- Daftar Tamu Undangan Makan Malam Terakhir ---")
print(f"Halo {tamu[0]}, saya masih mengundang Anda untuk makan malam di rumah saya.")
print(f"Halo {tamu[1]}, saya masih mengundang Anda untuk makan malam di rumah saya.")
del tamu[0]
del tamu[0]
print("--- Daftar tamu undangan makan malam sekarang: ---", tamu)