Python’ın 3.x öncesi sürümlerinde sınıflar yeni ve eski tip olmak üzere ikiye ayrılıyordu. Bu
sürümlerde eski tip sınıflar şöyle tanımlanıyordu:

Eski Tip Sinif : 

    class Sınıf:
        pass

    veya:

    class Sınıf():
    pass

Yeni Tip Sinif : 
    class Sınıf(object):
        pass

Yani eski tip sınıflar öntanımlı olarak herhangi bir taban sınıftan miras almazken, yeni
tip sınıfların object adlı bir sınıftan miras alması gerekiyordu. 

Dolayısıyla, tanımladığınız bir sınıfta object sınıfını miras almadığınızda, 
yeni tip sınıflarla birlikte gelen özelliklerden yararlanamıyordunuz. 

Mesela önceki derslerde öğrendiğimiz @property bezeyicisi yeni tip sınıflarla gelen bir özelliktir. 

Eğer Python 3 öncesi bir sürüm için kod yazıyorsanız ve eğer @property bezeyicisini kullanmak istiyorsanız 
tanımladığınız sınıflarda açık açık object sınıfını miras almalısınız.


Python 3’te ise bütün sınıflar yeni tip sınıftır. Dolayısıyla object sınıfını miras alsanız da
almasanız da, tanımladığınız bütün sınıflar öntanımlı olarak object sınıfını miras alacaktır.
Yani Python 3 açısından şu üç tanımlama arasında bir fark bulunmaz:
class Sınıf:
    pass
class Sınıf():
    pass
class Sınıf(object):
    pass
