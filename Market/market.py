print("Market programına hoşgeldiniz.")
print("Bu program sizin market alışverişlerinizde fiyatı hesaplar")
print("Size yardımcı olabileceğimiz ürünler şunlardır: SÜT - EKMEK - PİRİNÇ - MAKARNA - SU ")
def market() :
    toplam = 0
    ürün = input("Almak istediğiniz ürünü yazınız: ")
    sayı = int(input("Üründen kaç tane istediğinizi yazınız: "))
    if ürün == "süt" :
        toplam += sayı * 5
    elif ürün == "su" :
        toplam += sayı * 1.5
    elif ürün == "ekmek" :
        toplam += sayı * 1.5
    elif ürün == "pirinç" :
        toplam += sayı * 15
    elif ürün == "makarna" :
        toplam += sayı * 8.5
    bitir_devam = input("bitirmek için b ye basın devam etmek için d   ye basın: ")
    if bitir_devam == "d" :
        toplam += market()
    return toplam



toplam = market()
print(f"Su ana kadar yaptığını alışveris toplmı {toplam}")