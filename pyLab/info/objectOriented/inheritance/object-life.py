
Python’da bir sınıfın ömrü üç aşamadan oluşur:
1. İnşa (Construction)
2. İlklendirme (initialization)
3. Sonlandırma (destruction)


 __new__() Metodu : : : 

    bir sınıf örneklendiğinde çalışan ilk metot aslında __init__() değildir.
    inşa işleminden sorumlu metodun adı ise __new__()‘dur.

class Sınıf():
    def __new__(cls):
        pass
    def __init__(self):
        print('merhaba sınıf')

__new__() metodunun öntanımlı davranışını taklit etmek isterseniz : 

class Sınıf():
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)
    def __init__(self):
        print('merhaba sınıf')

"""
Burada yaptığımız şeyin aslında temel olarak basit bir miras alma işleminden ibaret olduğunu
görüyor olmalısınız. Bildiğiniz gibi, Python’daki bütün sınıflar, eğer başka bir sınıfı miras
olarak almıyorlarsa, otomatik olarak object sınıfını miras alırlar. Yani aslında yukarıdaki sınıf
tanımını Python şöyle görür:

"""


class Sınıf():
    def __new__(cls, *args, **kwargs):
        print('Yeni sınıf inşa edilirken lütfen bekleyiniz...')
        return object.__new__(cls, *args, **kwargs)
    def __init__(self):
        print('merhaba sınıf')