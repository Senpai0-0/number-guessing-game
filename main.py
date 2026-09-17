import random

def sayi_tahmin_oyunu():
    # 1. Bilgisayarın rastgele sayı seçmesi ve değişkenlerin tanımı
    hedef_sayi = random.randint(1, 100)
    tahmin_hakki = 7
    deneme_sayisi = 0

    print("=== SAYI TAHMİN OYUNU ===")
    print(f"1 ile 100 arasında bir sayı tuttum. Toplam {tahmin_hakki} tahmin hakkınız var.\n")

    # 2. Ana oyun döngüsü
    while deneme_sayisi < tahmin_hakki:
        try:
            # Kullanıcıdan girdi alma
            tahmin = int(input(f"({deneme_sayisi + 1}. Tahmin) Bir sayı giriniz: "))
        except ValueError:
            # Sayı dışı veri girişini engelleme
            print("Lütfen geçerli bir tam sayı girin!\n")
            continue

        deneme_sayisi += 1

        # 3. Tahmin kontrolü ve yönlendirme
        if tahmin < hedef_sayi:
            print("Daha YÜKSEK bir sayı söyleyin. ⬆️\n")
        elif tahmin > hedef_sayi:
            print("Daha DÜŞÜK bir sayı söyleyin. ⬇️\n")
        else:
            print(f"🎉 Tebrikler! {hedef_sayi} sayısını {deneme_sayisi}. denemede doğru bildiniz!")
            break
    else:
        # Hak bittiğinde çalışacak blok
        print(f"❌ Tahmin hakkınız bitti! Doğru sayı: {hedef_sayi} idi.")

if __name__ == "__main__":
    sayi_tahmin_oyunu()
    #İlk projem AI kullandım deneme ve mantık öğrenmek için :)