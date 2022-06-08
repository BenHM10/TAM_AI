print("Kondisi Gunung Berapi Saat Ini")
print("------------------------------")

sp = int(input('Masukkan suhu: '))
def suhuPermukaan(statusSuhu):
    if sp <= 35:
        statusSuhu = 'Normal'
    elif sp > 35 and sp <=38:
        statusSuhu = 'Waspada'
    elif sp <=40:
        statusSuhu = 'Siaga'
    elif sp > 40:
        statusSuhu = 'Awas'
    else:
        statusSuhu = 'Aman'
    return statusSuhu

sr = int(input('Masukkan magnitudo: '))

def magnitude(statusGempa):
    if sr < 3:
        statusGempa = 'Normal'
    elif sr < 4 and sr >=3:
        statusGempa = 'Waspada'
    elif sr < 6 and sr >=4:
        statusGempa = 'waspada'
    elif sr > 6:
        statusGempa = 'Awas'
    else:
        statusGempa = 'Tidak ada gempa'
    return statusGempa

print("Suhu  : ", suhuPermukaan)
print("Status Gempa : ", magnitude)
