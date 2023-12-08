import random

hak = 3

while hak > 0:
    oyuncu_secim = input("Tas mi, kagit mi, makas mi? ").lower()

    if oyuncu_secim in ['tas', 'kagit', 'makas']:
        bilgisayar_secim = random.choice(['tas', 'kagit', 'makas'])
        print(f"Bilgisayarın seçimi: {bilgisayar_secim}")

        if oyuncu_secim == bilgisayar_secim:
            print("Berabere!")
        elif (oyuncu_secim == 'tas' and bilgisayar_secim == 'makas') or \
             (oyuncu_secim == 'kagit' and bilgisayar_secim == 'tas') or \
             (oyuncu_secim == 'makas' and bilgisayar_secim == 'kagit'):
            print("Oyuncu kazandı!")
        else:
            print("Bilgisayar kazandı!")

        hak -= 1
        if hak > 0:
            print(f"{hak} hakkınız kaldı.")
        else:
            print("Haklarınız bitti. Oyun sona erdi.")
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen taş, kağıt veya makas seçin.")

if hak == 0:
    devam = input("Oyun tamamlandı. Tekrar oynamak ister misiniz? (evet/hayır): ").lower()
    if devam == 'evet':
        hak = 3
        print("Yeni oyun başlıyor...")
    else:
        print("Oyun sona erdi. İyi günler!")
