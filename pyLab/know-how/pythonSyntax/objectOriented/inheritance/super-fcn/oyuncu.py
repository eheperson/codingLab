class Oyuncu():
    """
    Üst sınıf kavramının İngilizcesi super class ‘tır. 
    İşte bu bölümde inceleyeceğimiz super() fonksiyonunun adı da buradaki ‘super’, yani ‘üst’ kelimesinden gelir. 
    Miras alınan üst sınıfa atıfta bulunan super() fonksiyonu, 
    miras aldığımız bir üst sınıfın nitelik ve metotları üzerinde 
    değişiklik yaparken, mevcut özellikleri de muhafaza edebilmemizi sağlar.
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
    def __init__(self, isim, rütbe):
        super().__init__(isim, rütbe)
        self.güç = 100

class İşçi(Oyuncu):
    def __init__(self, isim, rütbe):
        super().__init__(isim, rütbe)
        self.güç = 70

class Yönetici(Oyuncu):
    def __init__(self, isim, rütbe):
        super().__init__(isim, rütbe)
        self.güç = 20

"""
eğer taban sınıfın __init__() metodundaki parametre listesini alt sınıfta da tek tek tekrar etmek rahatsız ediyorsa :

class Asker(Oyuncu):
    def __init__(self, *arglar):
        super().__init__(*arglar)
        self.güç = 100
class İşçi(Oyuncu):
    def __init__(self, *arglar):
        super().__init__(*arglar)
        self.güç = 70
class Yönetici(Oyuncu):
    def __init__(self, *arglar):
        super().__init__(*arglar)
        self.güç = 20

Tek ve çift yıldızlı argümanlar genellikle şu şekilde gösterilir:

class Asker(Oyuncu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.güç = 100
"""

"""
Bu arada, miras alınan taban sınıfa atıfta bulunan super() fonksiyonu, Python programlama
diline sonradan eklenmiş bir özelliktir. Bu fonksiyon gelmeden önce taban sınıfa atıfta
bulunabilmek için doğrudan o sınıfın adını kullanıyorduk:

class Asker(Oyuncu):
    def __init__(self, isim, rütbe):
        Oyuncu.__init__(self, isim, rütbe)
        self.güç = 100

veya:

class Asker(Oyuncu):
    def __init__(self, *args):
        Oyuncu.__init__(self, *args)
        self.güç = 100


"""