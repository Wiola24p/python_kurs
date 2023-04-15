from produkty import Produkt
from koszyk import Koszyk

def main():
    Produkt.wczytaj_produkty("ceny.csv")
    #print(Produkt.produkt("Ser twarogowy - za 1 kg").cena(1,2021))
    koszyk=Koszyk()
    koszyk.dodaj(Produkt.produkt("Ser twarogowy - za 1 kg"))
    koszyk.dodaj(Produkt.produkt("Ser twarogowy - za 1 kg"))


if __name__ == "__main__":
     main()