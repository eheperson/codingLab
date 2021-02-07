"""
Python’da her şey bir nesnedir. 
Python’da nesneler ‘birinci sınıf öğeler’dir.  <first class>

Programlama dillerinde herhangi bir öğenin birinci sınıf bir öğe olması, o öğenin, dil içindeki
herhangi bir değer ile aynı kabiliyetlere sahip olması anlamına gelir.

Python’daki sınıf yapılarının ‘birinci sınıf’ öğeler olması, 
bu yapıların, dil içindeki öteki değerlerle aynı özelliklere ve 
kabiliyetlere sahip olması demektir. Yani Python’daki sınıflar şu özelliklere sahiptir:
    1. Başka bir fonksiyona veya sınıfa parametre olarak atanabilirler
    2. Bir fonksiyondan döndürülebilirler
    3. Bir değişkene atanabilirler

Yani, bir öğenin ‘birinci sınıf’ olması demek, 
dil içindeki başka öğelerle yapabildiğiniz her şeyi
o öğeyle de yapabilmeniz demektir.


        Guido Van Rossum : 
            Python’a ilişkin hedeflerimden bir tanesi de, bu dili, bütün nesneler “birinci sınıf”
            olacak şekilde tasarlamaktı. Bununla kastettiğim, dil içinde kendisine bir isim
            verilebilen bütün nesnelerin (örn. tam sayılar, karakter dizileri, fonksiyonlar,
            sınıflar, modüller, metotlar, vb.) eşit statüye sahip olmasıdır. Yani, bütün
            nesnelerin değişkenlere atanabilmesi, listelerin içine yerleştirilebilmesi, sözlükler
            içinde depolanabilmesi, argüman olarak atanabilmesi ve saire...

"""
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
class Sınıf():
    # Python’da baş tarafında yukarıdaki gibi iki adet alt çizgi olan, 
    # ancak uç tarafında alt çizgi bulunmayan
    # (veya yalnızca tek bir alt çizgi bulunan) 
    # bütün öğeler birer gizli üyedir
    __gizli = 'gizli'

    def örnek_metodu(self):
        print(self.__gizli)
        print('örnek metodu')

    @classmethod
    def sınıf_metodu(cls):
        print('sınıf metodu')

    @staticmethod
    def statik_metot():
        print('statik metot')

"""
Sınıf Üyeleri
Python’da bir sınıf içinde bulunan nitelikler, değişkenler, metotlar, fonksiyonlar ve 
buna benzer başka veri tipleri, o sınıfın üyelerini meydana getirir.

Bir sınıfın üyelerini genel olarak üçe ayırarak inceleyebiliriz:
    • Aleni üyeler (public members )
    • Gizli üyeler (private members )
    • Yarı-gizli üyeler (semi-private members )


Eğer bir sınıf üyesi dışarıya açıksa, yani bu üyeye sınıf dışından normal yöntemlerle
erişilebiliyorsa bu tür üyelere ‘aleni üyeler’ adı verilir.
( dir() komutunun çıktısında görünen ve normal yollardan erişebildiğimiz bütün öğeler )

Aleni üyelerin aksine gizli üyeler dışarıya açık değildir. Gizli üyelere, normal
yöntemleri kullanarak sınıf dışından erişemeyiz.
Bir üyenin gizli olabilmesi için başında en az iki adet, ucunda da en fazla bir adet alt çizgi bulunmalıdır. 

Yarı-gizli üyeler, herhangi bir özel mekanizma aracılığıyla değil de yalnızca topluluk içi
gelenekler tarafından korunan niteliklerdir. Herhangi bir üyeyi yarı-gizli olarak işaretlemek
için yapmamız gereken tek şey başına bir adet alt çizgi yerleştirmektir.
Buradaki _yarıgizli adlı niteliğe sınıf içinden veya dışından erişmemizi engelleyen veya
zorlaştıran hiçbir mekanizma bulunmaz. Ama biz bir sınıf içinde tek alt çizgi ile başlayan
bir öğe gördüğümüzde, bunun sınıfın iç işleyişine ilişkin bir ayrıntı olduğunu, sınıf dışından
bu öğeyi değiştirmeye kalkışmamamız gerektiğini anlarız.

İsim Bulandırma
Python’da gerçek anlamda gizli ve dışarıya tamamen kapalı üyeler bulunmaz. 

s = sinif.Sinif()
s._Sinif__gizli

Python, siz bir sınıf üyesini __gizli şeklinde tanımladığınızda, bu öğe üzerinde şu işlemleri gerçekleştirir:
    Öncelikle değişkenin baş tarafına bir alt çizgi ekler:
        _
    Daha sonra, bu alt çizginin sağ tarafına bu gizli üyeyi barındıran sınıfın adını iliştirir:
        _Sınıf

    Son olarak da gizli üyeyi sınıf adının sağ tarafına yapıştırır:
        _Sınıf__gizli

"""
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
class Sınıf2():
    sınıf_niteliği = 0

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        self.örnek_niteliği = 0

    def örnek_metodu(self):
        self.örnek_niteliği += 1
        return self.örnek_niteliği

    @classmethod
    # @classmethod bezeyicisi fonksiyonu sınıf metoduna dönüştürme işlevi görüyor.
    def sınıf_metodu(cls):
        cls.sınıf_niteliği += 1
        return cls.sınıf_niteliği

    @staticmethod
    # statik metotları tanımlamak için @staticmethod bezeyicisini kullanıyoruz
    # sınıfın herhangi bir niteliğine erişmesine gerek olmayan fonksiyonları, 
    # sınıf dışına atmak yerine, birer statik metot olarak sınıf içine yerleştirebiliriz.
    # Statik metotları hem örnekler hem de sınıf adları üzerinden kullanabiliriz.
 
    def statik_metot():
        print('merhaba statik metot!')
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
class Mat():
    '''Matematik işlemleri yapmamızı sağlayan
    bir sınıf.

    Burada Mat() adlı bir sınıf tanımladık. 
    Bu sınıf içinde iki adet statik metodumuz var: 
        pi()
        karekök(). 

    Bu iki fonksiyon, örnek ve sınıf metotlarının aksine ilk parametre olarak self veya cls almıyor. 
    Çünkü bu iki sınıfın da sınıf veya örnek nitelikleriyle herhangi bir işi yok.   
    '''

    @staticmethod
    def pi():
        return 22/7

    @staticmethod
    def karekök(sayı):
        return sayı ** 0.5
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
class Calisan():
    personel = [] #sinif niteligi
    # self.n = 0 > hata

    def __init__(self,isim): #ornek metodu
        self.isim = isim #ornek niteligi
        self.kabiliyetleri=[] #ornek niteligi
        self.personele_ekle() #ornek niteligi

    @classmethod
    def personel_sayisini_gorutule(cls):#sinif metodu
        print(len(cls.personel))

    def personele_ekle(self):#ornek metodu
        self.personel.append(self.isim)
        print("{} adli kisi personele eklendi".format(self.isim))

    @classmethod
    def personeli_goruntule(cls):#sinif metodu
        print('Personel Listesi : ')
        for kisi in cls.personel:
             print(kisi)

    def kabiliyet_ekle(self,kabiliyet):#ornek metodu
        self.kabiliyetleri.append(kabiliyet)

    def kabiliyetleri_goruntule(self):#ornek metodu
        print('{} adli kisinin kabiliyetleri : '.format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)

"""
Biz ahmet.kabiliyetleri şeklinde bir komut verdiğimizde, Python ilk olarak ilgili sınıfın
__init__() fonksiyonu içinde kabiliyetleri adlı bir örnek niteliği arar. Elbette Python’ın
bu örnek niteliğini bulabilmesi için, __init__() fonksiyonu içinde, bu fonksiyonun ilk
parametresi ile aynı öneki taşıyan bir niteliğin yer alması gerekir. Yani eğer __init__()
fonksiyonunun ilk parametresi self ise, Python bu fonksiyon içinde self.kabiliyetleri adlı bir
örnek niteliği bulmaya çalışır. Eğer bulamazsa, Python bu kez kabiliyetleri adlı bir sınıf niteliği
arar. Eğer onu da bulamazsa tabii ki hata verir

class Çalışan():
    kabiliyetleri = ['sınıf niteliği']
    def __init__(self):
        self.kabiliyetleri = ['örnek niteliği']

Böyle bir durumda, yukarıda bahsettiğimiz mekanizma nedeniyle, self.kabiliyetleri
şeklinde ifade ettiğimiz örnek niteliği, kabiliyetleri adlı sınıf niteliğini gölgeler. Bu yüzden de
print(ahmet.kabiliyetleri) komutu, örnek niteliğini, yani self.kabiliyetleri listesini verir.

Sınıf niteliği olan kabiliyetleri listesine erişmek
için, sınıf örneğini değil de, sınıf adını kullanacaksınız:

class Çalışan():
    kabiliyetleri = ['sınıf niteliği']
    def __init__(self):
        self.kabiliyetleri = ['örnek niteliği']

#sınıf niteliğine erişmek için
#sınıf adını kullanıyoruz
print(Çalışan.kabiliyetleri)

#örnek niteliğine erişmek için
#örnek adını kullanıyoruz
ahmet = Çalışan()
print(ahmet.kabiliyetleri)

Python’ın söz dizimi kuralları açısından, eğer bir örnek niteliği tanımlıyorsak, bu
niteliğin başına bir self getirmemiz gerekir. Ayrıca bu self kelimesini de, örnek niteliğinin
bulunduğu fonksiyonun parametre listesinde ilk sıraya yerleştirmiş olmalıyız. Unutmayın,
örnek nitelikleri sadece fonksiyonlar içinde tanımlanabilir. Fonksiyon dışında örnek niteliği
tanımlayamazsınız. Yani şöyle bir şey yazamazsınız:
class Çalışan():
    self.n = 0
    def __init__(self):
        self.kabiliyetleri = []


"""
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
class Falanca():
    nitelik = 'nitelik'

    def __init__(self):
        self.nitelik = 'nitelik'
        self.ver = '0.1'
        self._sayi = 0

    def örnek_fonk(self):
        pass

    @classmethod
    def sınıf_fonk(cls):
        pass

    @staticmethod
    def statik_fonk():
        pass

    @property
    # Burada versiyon() adlı metodu @property bezeyicisi ile ‘bezedik’. 
    # Böylece bu metodu bir ‘nitelik’ haline getirmiş olduk. 
    # Artık bunu şöyle kullanabiliriz:
    #
    # program = Program()
    # program.versiyon
    #
    # ver değişkenini salt okunur hale getirdi.
    def versiyon(self):
        return self.ver

    @property
    def sayı(self):
        return self._sayı

    @sayı.setter
    # Eğer amacınız değişkeni salt okunur hale getirmek değilse 
    # @property ile bezediğimiz fonksiyon için bir setter parametresi tanımlayabilirsiniz.
    def sayı(self, yeni_değer):
        self._sayı = yeni_değer
        return self._sayı

    @sayı.deleter
    # .setter dışında .deleter adlı özel bir @property bezeyicisi daha bulunur. 
    # Bunu da bir değeri silmek için kullanıyoruz:
    def sayı(self):
        del self._sayı
"""
Metottan Niteliğe

Property kelimesi (attribute kelimesine benzer bir şekilde) İngilizcede ‘özellik, nitelik’ gibi anlamlara gelir. 
Kelime anlamına uygun olarak, @property bezeyicisinin yaptığı en temel iş, bir metodu, nitelik gibi kullanılabilecek hale getirmektir.

@property bezeyicisinin üç önemli işlevi bulunur:
    • Değer döndürmek
    • Değer atamak
    • Değer silmek

Gördüğünüz gibi, @property bezeyicisini kullanırken üç ayrı metot tanımlıyoruz:
• İlgili niteliğe nasıl ulaşacağımızı gösteren bir metot: Bu metodu @property ile beziyoruz.
• İlgili niteliği nasıl ayarlayacağımızı gösteren bir metot: Bu metodu @metot_adı.setter şeklinde beziyoruz.
• İlgili niteliği nasıl sileceğimizi gösteren bir metot: Bu metodu @metot_adı.deleter şeklinde beziyoruz.
"""
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
