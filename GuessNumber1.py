
import random

print("Merhaba! Bir sayı tahmin oyununa hoş geldiniz.")

# Rastgele bir sayı seç
sayi = random.randint(1, 100)
#Kaçıncı denemede bildiğini söyle.
deneme=0
# Oyun döngüsü
while True:
    tahmin = int(input("1 ile 100 arasında bir sayı tahmin edin: "))

    # Tahminin doğruluğunu kontrol et
    if tahmin == sayi:
        print(f"Tebrikler! {deneme}. denemede {sayi} sayısını doğru tahmin ettiniz.")
        break
    elif tahmin < sayi:
        print("Daha büyük bir sayı tahmin edin.")
        deneme+=1
    else:
        print("Daha küçük bir sayı tahmin edin.")
        deneme+=1


