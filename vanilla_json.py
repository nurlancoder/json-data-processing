import json
import os

def json_dosyasini_kontrol_et(dosya_yolu):
    if not os.path.exists(dosya_yolu):
        print(f"JSON dosyası bulunamadı: {dosya_yolu}")
        return None

    try:
        with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
            veri = json.load(dosya)
            print("JSON dosyası başarıyla yüklendi.")
            return veri
    except json.JSONDecodeError as e:
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
print("JSON Verisi (Vanilla Python):")
print(veri)

# Belirli bir alanı değiştirme
if isinstance(veri, list) and len(veri) > 0 and 'isim' in veri[0]:
    veri[0]['isim'] = 'Ahmet'
    print("\nİlk kişinin ismi Ahmet olarak güncellendi:")
    print(veri[0])
else:
    print("Veri beklenen formatta değil ya da boş.")

# Yaşı 30'dan büyük olanları filtreleme
yas_30_ustu = [kisi for kisi in veri if isinstance(kisi, dict) and 'yas' in kisi and kisi['yas'] > 30]
print("\nYaşı 30'dan büyük olanlar:")
print(yas_30_ustu)

# Güncellenen veriyi yeni bir dosyaya kaydetme
try:
    with open('veri_guncel.json', 'w', encoding='utf-8') as dosya:
        json.dump(veri, dosya, ensure_ascii=False, indent=4)
    print("\nGüncellenmiş veri 'veri_guncel.json' dosyasına başarıyla kaydedildi.")
except Exception as e:
    print(f"Veri dosyası kaydedilemedi: {e}")
