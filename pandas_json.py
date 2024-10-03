import pandas as pd
import os

def json_dosyasini_kontrol_et(dosya_yolu):
    if not os.path.exists(dosya_yolu):
        print(f"JSON dosyası bulunamadı: {dosya_yolu}")
        return None

    try:
        # JSON dosyasını oku ve DataFrame'e yükle
        veri = pd.read_json(dosya_yolu)
        print("JSON dosyası başarıyla yüklendi.")
        return veri
    except ValueError as e:
        print(f"JSON format hatası: {e}")
    except Exception as e:
        print(f"Dosya okunurken bir hata oluştu: {e}")

    return None

# JSON dosyası yolu
dosya_yolu = r'C:\Users\User\Desktop\Veri json\veri.json'

print("Kod başlıyor...")

# JSON dosyasını kontrol et ve yükle
veri = json_dosyasini_kontrol_et(dosya_yolu)

if veri is None:
    print("Program sonlandırılıyor. JSON dosyasında bir sorun var.")
    exit()

# JSON verisini yazdırma
print("JSON Verisi (Pandas):")
print(veri)

# İlk kişinin ismini güncelleme
veri.loc[0, 'isim'] = 'Ahmet'
print("\nİlk kişinin ismi Ahmet olarak güncellendi:")
print(veri.iloc[0])

# Yaşı 30'dan büyük olanları filtreleme
yas_30_ustu = veri[veri['yas'] > 30]
print("\nYaşı 30'dan büyük olanlar:")
print(yas_30_ustu)

# Güncellenen veriyi yeni bir dosyaya kaydetme
try:
    veri.to_json('veri_guncel.json', orient='records', force_ascii=False, indent=4)
    print("\nGüncellenmiş veri 'veri_guncel.json' dosyasına başarıyla kaydedildi.")
except Exception as e:
    print(f"Veri dosyası kaydedilemedi: {e}")
