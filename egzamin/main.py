from produkty import Produkt

def main():
    Produkt.wczytaj_produkty("ceny.csv")
    print(Produkt.produkt("Ser twarogowy - za 1 kg").get_nazwa())


if __name__=="__main__":
    main()