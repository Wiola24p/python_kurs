class Koszyk:
    def __init__(self):
        self._produkty={}

    def dodaj(selfself,produkt):
        if produkt.get_nazwa() in self._produkty.keys():
            self._produkty[produkt.get_nazwa()] =produkt,self._produkty[produkt.get_nazwa()](1)+1
        else:
            self._produkty[produkt.get_nazwa()] =  produkt, 1
