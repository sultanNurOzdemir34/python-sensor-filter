# Basit bir sıcaklık verisi filtreleme ve eşik kontrol simülasyonu

def sensor_verisini_isle(sicaklik_listesi, esik_deger):
    print(f"--- Sistem Aktif (Eşik Değer: {esik_deger}°C) ---")
    anomaliler = []
    
    for i, sicaklik in enumerate(sicaklik_listesi):
        if sicaklik > esik_deger:
            print(f"Uyarı [{i}. Ölçüm]: Kritik sıcaklık tespit edildi -> {sicaklik}°C")
            anomaliler.append((i, sicaklik))
        else:
            print(f"Normal [{i}. Ölçüm]: {sicaklik}°C")
            
    return anomaliler

# Örnek sensörden gelen sıcaklık akışı (simülasyon)
gelen_veriler = [22.5, 23.0, 24.2, 35.8, 23.5, 41.2, 22.8]
kritik_sinir = 30.0

# Fonksiyonu çalıştır
tespit_edilenler = sensor_verisini_isle(gelen_veriler, kritik_sinir)
print(f"\nToplam anomali sayısı: {len(tespit_edilenler)}")