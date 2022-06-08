from logging import NullHandler


print("Kondisi Gunung Berapi Saat Ini")
print("------------------------------")

sp = int(input('Masukkan suhu: '))
def suhuPermukaan(sp):
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

def magnitude(sr):
    if sr < 3:  
        statusGempa = 'Normal'
    elif sr < 4 and sr >=3:
        statusGempa = 'Waspada'
    elif sr < 6 and sr >=4:
        statusGempa = 'Siaga'
    elif sr >= 6:
        statusGempa = 'Awas'
    else:
        statusGempa = 'Tidak ada gempa'
    return statusGempa

print("Suhu : ", suhuPermukaan(sp))
print("Status Gempa : ", magnitude(sr))

def prediksiGB(sp, sr):
    if sp <35 and sr < 3:
        prediksi = "Status Aman"
    elif sp <35 and sr < 4 and sr >= 3:
        prediksi = "Status Aman"
    elif sp > 35 and sp <= 38 and sr < 3:
        prediksi = "Status Aman"
    elif sp > 35 and sp <=38 and sr < 4 and sr >=3:
        prediksi = "Status Waspada"
    elif sp <=40 and sr < 4 and sr >= 3:
        prediksi = "Status Waspada"
    elif sp > 35 and sp <=38 and sr < 6 and sr >=4:
        prediksi = "Status Waspada"
    elif sp <=40 and sr <6 and sr >4:
        prediksi = "Status Siaga"
    elif sp <=40 and sr > 6:
        prediksi = "Status Siaga"
    elif sp > 40 and sr > 6:
        prediksi = "Status Awas"
    elif sp <=35 and sr < 6 and sr >=4:
        prediksi = "Status Waspada"
    elif sp <=35 and sr > 6:
        prediksi = "Status Waspada"
    elif sp > 35 and sp <=38 and sr >6:
        prediksi = "Status Waspada"
    else:
        prediksi = "Belum Ada Prediksi"
    return prediksi

print("Prediksi : ", prediksiGB(sp,sr))
