# -*- coding: utf-8 -*-

def toplam_carpim_ve_yuze_bol(liste1, liste2):
    """
    İki listeyi sırayla çarpar, sonuçları toplar ve 100'e böler.
    
    :param liste1: İlk sayıların listesi.
    :param liste2: İkinci sayıların listesi (çarpanlar).
    :return: Toplam çarpım sonucunun 100'e bölünmüş hali.
    """
    if len(liste1) != len(liste2):
        raise ValueError("İki listenin uzunluğu aynı olmalıdır.")
    
    toplam = 0
    for i in range(len(liste1)):
        toplam += liste1[i] * liste2[i]
    
    sonuc = toplam / 100
    return sonuc

def main():
    while True:
        # Kullanıcı dostu arayüz
        print("Lütfen notlarinizi arada virgül olacak sekilde girin.:")
        print("Örneğin: 100,70,81,75,71,100,90,42,65,77,33,90,90")
        girilen_degerler = input()
        liste1 = [int(x) for x in girilen_degerler.split(',')]

        # İkinci liste sabit kalacak
        liste2 = [2.5, 10, 3, 5, 20, 2.5, 10, 5, 5, 20, 10, 4, 3]

        sonuc = toplam_carpim_ve_yuze_bol(liste1, liste2)
        print("Sonuç:", sonuc)

        devam = input("Yeniden işlem yapmak istiyor musunuz? (E/H): ")
        if devam.upper() != 'E':
            break

if __name__ == "__main__":
    main()
