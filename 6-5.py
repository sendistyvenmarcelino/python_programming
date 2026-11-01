sungai = {
    'nil' : 'mesir',
    'amazon' : 'brazil',
    'bengawan solo' : 'indonesia'
}
for s, negara in sungai.items():
    print(f"Sungai {s.title()} berada di negara {negara.title()}.")
print("\nDaftar sungai yang disebutkan:")
for s in sungai.keys():
    print(f"- {s.title()}")
print("\nDaftar negara yang disebutkan:")
for negara in sungai.values():
    print(f"- {negara.title()}")    