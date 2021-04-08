/**         
 *      WITH ES6
 * 
 * 
 *  JAvascript uses Prototype method to create object, There is no classes in prototype method,
 *  Instead, you create new objects using some kind of copying method.
 * 
 *  However, when using function constructors, these functions can be thought of as class definitions.
 * 
 * 
 *  With ES6, declaration method has been added.
 *  In this method, we could define a class like in some other programming languages 
 *  (but JavaScript still uses the prototype method). 
 *  We use the new operator to create an instance of the class also.
 * 
 * 
 *  In class definitions made in this way, the class will have a prototype property just like the function constructor.
 * 
 */
// Class Example
class Creature{};
  
// Instance of Class
var c1 = new Creature();

//adding a new property to class ( not to the instance)
Creature.prototype.name = "Undefined";
 
//adding a new method to class ( not to the instance)
Creature.prototype.speak = function() {
    console.log("Ellooo I am " + this.name);
};
 
// Another instance of Class
var c2 = new Creature();
c2.speak()

/*
    check the console.log(Creature.prototype.constructor);
*/

// ONE STEP FORWARD : Class with constructor

class CreatureV2 {
    constructor() {
        console.log("That is the constructor of CreatureV2 class");
    }
};
 
var c4 = new CreatureV2()
 
// check
console.log(CreatureV2.prototype.constructor);

/*
function CreatureV2() {
    console.log("Cnstructor Function");
};
 
var c = new CreatureV2();
console.log(Creature.prototype.constructor);

that is same with : 
        class CreatureV2 {
            constructor() {
                console.log("That is the constructor of CreatureV2 class");
            }
*/
Sınıf içinde örneklerin özellik değerlerinin farklı belirlenebilmesi veya ön hazırlıkta kullanılması için, constructor fonksiyonunda parametreler kullanabilirsiniz.


 
var kedi = new Canli("Pati");
var kopek = new Canli("Karabaş");
 
console.log(kedi.adi);    // Pati yazar.
console.log(kopek.adi);   // Karabaş yazar.

Sınıf Bildirimlerinde Getter ve Setter Fonksiyonlar
this.adi şeklinde nokta gösterimi kullanarak özelliğe değer atamak veya döndürmek yerine getter ve setter fonksiyonlar tanımlayabilirsiniz. getter fonksiyonlar, özelliğin değeri istendiğinde, setter fonksiyonlar ise özelliğin değeri değiştirilmek istendiğinde çalıştırılır.

Örneğin;
kedi.Adi = "Yumak";
şeklinde bir ifade Adi özelliğinin değerini Yumak yapar ve bunun için setter olarak (set ile) tanımlanan fonksiyonu çalıştırır.

console.log(kedi.Adi);
şeklinde bir ifade ise Adi özelliğinin son değerini verir ve bunun için getter olarak (get ile) tanımlanan fonksiyonu çalıştırır.

Özelliğin adı getter veya setter fonksiyona verilen ad olacaktır.

class Canli {
	constructor(adi) {
		this.adi = adi;
	}
	get Adi() {
		return this.adi;
	}
	set Adi(yeniAd) {
		this.adi = yeniAd;
	}
}
 
var kedi = new Canli("Pati");
 
// get Adi() {...} şeklinde tanımlanan fonksiyon çalıştırılır ve adi özelliğinin değeri döndürülür
console.log(kedi.Adi); 
 
// set Adi(yeniAd) {...} şeklinde tanımlanan fonksiyon çalıştırılır. Yeni ad parametresinin değeri
// özelliğe atanan değer (Yumak) olur.
 
kedi.Adi = "Yumak";
console.log(kedi.Adi);
kedi.Adi şeklindeki ifadede Adi özelliğinin fonksiyon tanımındaki gibi baş harfi büyük yazıldığına dikkat edin. Bu adi özelliği (baş harfi küçük olan) değildir. Örnekteki baş harfi büyük ve küçük yazılan özellik adları benim tercihimdir. adi özelliği asıl değeri tutacak olan özellik, Adi şeklinde tanımlanan fonksiyonlar ise bu özelliğin değerini değiştirmek veya döndürmek için kendiliğinden çalıştırılan fonksiyonlardır.
Sınıf Bildirimlerinde Yöntem (Metot) Tanımlama
Sınıfın yöntemlerini tanımlamak için function ifadesini yazmadan doğrudan fonksiyon adı yazıp tanımlayın.

class Kisi {
	constructor(adi) {
		this.adi = adi;
	}
	// Bir yöntem tanımla.
	selamla() {
		console.log("Merhaba. Ben " + this.adi + ".");
	}
}
 
var ben = new Kisi("Ali");
 
ben.selamla();      // Merhaba. Ben Ali. yazar.
Sınıf bildirimlerinde yöntem tanımlarken, parantez gösterimini de kullanabilirsiniz. Parantez gösterimi için şuraya bakabilirsiniz.

class Kisi {
	constructor(adi) {
		this.adi = adi;
	}
 
	["selamla"]() {
		console.log("Merhaba. Ben " + this.adi + ".");
	}
}
 
var ben = new Kisi("Ali");
 
ben.selamla();      // Merhaba. Ben Ali. yazar.

Sınıf Bildirimlerinde Statik (static) Yöntem Tanımlama
Sınıf bildirimlerinde sınıfın örneğini oluşturmadan kullanabileceğiniz ve sınıfın örneği ile çağırılamayan statik metotlar tanımlayabilirsiniz.

Statik yöntemler, sınıfla doğrudan ilgili olan ancak sınıfın örneği (nesne) içinde bir işe yaramayan veya kullanılmayacak olan yöntemlerdir. Sınıfın örneği oluşturulduğunda örneğin bir üyesi olmazlar. Statik yöntemler kullanılarak sınıfla ilgili bazı genel amaçlı yöntemleri sınıf tanımlaması içinde yapar ve böylece bir bütünlük ve düzen sağlamış oluruz.

Örnek:
class Nokta {
	constructor(x, y) {
		this.x = x;
		this.y = y;
	}
	
	static ikiNoktaArasindakiUzaklik(nokta1, nokta2) {
		var xFarki = nokta1.x - nokta2.x;
		var yFarki = nokta1.y - nokta2.y;
		return Math.sqrt(xFarki * xFarki + yFarki * yFarki);
	}
}
 
var p1 = new Nokta(3, 5);
var p2 = new Nokta(30, 40);
 
var uzaklik = Nokta.ikiNoktaArasindakiUzaklik(p1, p2);
 
console.log(uzaklik);                       // 44.204072210600685 yazar.
console.log(p1.ikiNoktaArasindekiUzaklik);  // undefined yazar. Statik fonksiyonlar örnek ile çağırılamaz.
Bu örnekte iki şeye dikkat edin. Birincisi statik olarak tanımlanan fonksiyonun başına static ifadesi yazılmıştır. İkincisi ise 
var uzaklik = Nokta.ikiNoktaArasindakiUzaklik(p1, p2);
satırında p1 veya p2 örneklerinin değil, sınıfın adı (Nokta) yazılarak statik fonksiyon çağırılmıştır.

Örnekte, Nokta isimli bir sınıf ile x ve y koordinatları verilerek nokta tanımlanıyor. İki nokta arasındaki uzaklığı hesaplayan statik yöntem tanımlanıyor. Uzaklık hesaplayan fonksiyon oluşturulan örneklerin içinde herhangi bir göreve sahip değildir. Ancak tamamen Nokta sınıfı ile ilgili olan bir yöntemdir. Bu nedenle Nokta sınıfının içinde tanımlanmıştır.

Yine vurgulayalım, statik yöntemler çağırılırken oluşturulan örneğin / nesnenin (örneğimizde p1 ve p2) değil sınıfın adı (örneğimizde Nokta) kullanılır. Ve uyaralım. Statik yöntemlerin içinde constructor fonksiyonda yaptığımız gibi this kullanırsanız örneğe işaret etmez, global nesneye (web sayfalarında window nesnesine) işaret eder. Statik yöntemler içinde örneğin üyelerine (özellik ve yöntem) this ile ulaşamazsınız.

Sınıf Bildirimlerinde Kalıtım Uygulama (extends)
Nesneye yönelik programlamada, bir sınıfın tüm özellik ve yöntemlerini yeni özellik ve yöntemlerle genişletmek üzere devralan bir sınıf tanımlama işlemine kalıtım (inheritance) denir.

JavaScrpit ile bu işlemi extends ifadesini kullanarak yapabilirsiniz.

class Hayvan {
	constructor(adi) {
		this.adi = adi;
	}
	sesCikar() {
		console.log("Bir hayvan sesi.");
	}
}
 
// Kedi isimli bir sınıf tanımla (class Kedi) ve Hayvan sınıfının tüm özellik ve yöntemlerini al (extends Hayvan).
 
class Kedi extends
 Hayvan {
	// sesCikar fonksiyonunu yeniden tanımla (override)
	sesCikar() {
		console.log(this.adi + " miyavlıyor.");
	}
	// Burada kediye has yeni yöntemler de ekleyebilirsiniz...
}
 
// Kedi sınıfında yapılandırıcı olmadığından bu ifade Hayvan sınıfının yapılandırıcısını çağırır.
var pati = new Kedi("Pati");
 
pati.sesCikar();       // Pati miyavlıyor. yazar.
Nesneye yönelik programlamada bazen, türetilen yeni sınıf içinden, türetildiği ana sınıfın yöntemlerini çağırmak gerekebilir. JavaScript sınıf bildirimlerinde bunu super ifadesi ile yaparız. super kullanımı this kullanımına benzer. this oluşturulan örneğin (nesnenin) kendisine, super ise türetildiği sınıfa işaret eder.

class Hayvan {
	constructor(adi) {
		this.adi = adi;
	}
	sesCikar() {
		console.log("Bir hayvan sesi.");
	}
}
 
// Kedi isimli bir sınıf tanımla (class Kedi) ve Hayvan sınıfının tüm özellik ve yöntemlerini al (extends Hayvan).
 
class Kedi extends Hayvan {
	// ses cikar fonksiyonunu yeniden tanımla (override)
	sesCikar() {
		super.sesCikar();                         // Temel sınıfın sesCikar yöntemini çağır.
		console.log(this.adi + " miyavlıyor.");
	}
}
 
// Kedi sınıfında yapılandırıcı olmadığından bu ifade Hayvan sınıfının yapılandırıcısını çağırır.
var pati = new Kedi("Pati");
 
pati.sesCikar();
Çıktısı:

Bir hayvan sesi.
Pati miyavlıyor.

extends ile JavaScript'in yerleşik sınıflarını da (Array gibi) genişletebilirsiniz.

JavaScript'de Sınıf İfadeleri (Class Expressions)
Sınıf tanımlarını fonksiyon ifadelerde olduğu gibi bir ifade şeklinde de yapabilirsiniz. 
var Hayvan = class {
	constructor(adi) {
		this.adi = adi;
	}
};
Veya isim vererek de bir sınıf ifadesi yazabilirsiniz.
var Hayvan = class Hayvan {
	constructor(adi) {
		this.adi = adi;
	}
};
Ancak verdiğiniz isim (ikinci Hayvan), sadece sınıf içinde geçerli olacaktır.

Bu tanımlamalar bir ifade (Expression) olduğu için sonuna ; konulmuştur.

Özet Sınıf (Abstract Class) / Sınıf Şablonu Tanımlama
Nesneye yönelik programlamada özet sınıflar, kendilerinden türetilecek başka sınıfların kullanacağı ortak yöntem ve özellikleri tanımlayan şablonlardır. Bunu JavaScript sınıf bildirimi döndüren bir fonksiyon kullanarak şu şekilde oluşturabilirsiniz.

function OzetSinif(TemelSinif) {
    return class extends TemelSinif {
        sesCikar() {
            console.log(this.adi + " ses çıkarıyor.");
        }
    };
}
 
class Hayvan {
    constructor(adi) {
        this.adi = adi;
    }
}
 
class Kedi extends OzetSinif(Hayvan) {
    // Burada Kedi sınıfına özel yöntemler olabilir.
}
class Kopek extends OzetSinif(Hayvan) {
    // Burada Kopek sınıfına özel yöntemler olabilir.
}
 
var pati = new Kedi("Pati");
var karabas = new Kopek("Karabaş");
 
pati.sesCikar();
karabas.sesCikar();
Dilerseniz sınıf döndüren fonksiyonu ok fonksiyonu şeklinde de tanımlayabilirsiniz.
var OzetSinif = TemelSinif => class extends TemelSinif {
    sesCikar() {
        console.log(this.adi + " ses çıkarıyor.");
    }
};
 
class Hayvan {
    constructor(adi) {
        this.adi = adi;
    }
}
 
class Kedi extends OzetSinif(Hayvan) {
    // Burada Kedi sınıfına özel yöntemler olabilir.
}
class Kopek extends OzetSinif(Hayvan) {
    // Burada Kopek sınıfına özel yöntemler olabilir.
}
 
var pati = new Kedi("Pati");
var karabas = new Kopek("Karabaş");
 
pati.sesCikar();
karabas.sesCikar();

Bu kadar. Makaleyi henüz tam olarak kontrol etmedim. Eğer bir hata veya eksik görürseniz bildirin.