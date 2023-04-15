class Produkt:
    def__init__(self,linia):
    dane = linia.split(";")
    self._nazwa=dane[0]
    self._ceny=[float(cena) for cena in dane[1:]]

    new*
    def get_nazwa(self):
        return self._nazwa

    new*
    def get_cena(self):
        return self._cena



