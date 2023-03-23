import random

def computer_guess(x):
    low=1
    high=x
    aklindakisayi=""
    denemes=0
    while aklindakisayi != "d":
        Tahmin=random.randint(low,high)
        denemes+=1
        aklindakisayi=input(f"Aklındaki sayı {Tahmin} sayısından büyük mü(b) küçük mü(k) yoksa bu sayı mı?(d)")
        if aklindakisayi=="b":
            low = Tahmin
        elif aklindakisayi=="k":
            high = Tahmin
        else:
            print(f"Tuttuğun {Tahmin} sayısını {denemes}. denememde buldum.")

computer_guess(100)
