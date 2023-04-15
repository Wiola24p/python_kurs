from produkty import Produkt

def main():
    Produkt.wczytaj_produkty("ceny.csv")
    print(Produkt.produkt("Ser twarogowy - za 1 kg").cena(1,2021))


if __name__ == "__main__":
     main()