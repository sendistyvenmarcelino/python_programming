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
for tamu in tamu:
    print(f"Halo {tamu}, saya mengundang Anda untuk makan malam di rumah saya.")