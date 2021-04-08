class Oyuncu():
    """
    base class, super class or parent class
    """
    def __init__(self, isim, rütbe):
        self.isim = isim
        self.rütbe = rütbe
        self.güç = 0

    def hareket_et(self):
        print('hareket ediliyor...')

    def puan_kazan(self):
        print('puan kazanıldı')

    def puan_kaybet(self):
        print('puan kaybedildi')

class Asker(Oyuncu):
    """
    subclass or child class
    """
    pass

class İşçi(Oyuncu):
    """
    subclass or child class
    """
    pass

class Yönetici(Oyuncu):
    """
    subclass or child class
    """
    pass
