//bu mdul nodeJs ile dosya okuyup yazmamizi saglar

var fs = require('fs')

// Dosya Okuma islemleri
fs.readFile('dosya.txt',"utf8", function(hata, data){
    if(hata){
        throw hata;
    }

    console.log(data)
    // "utf8" belirtilmese idi string olarak veri almak icin
    // asagidaki format kullanilmali
    // console.log(data.toString())

    //console.log(data) olarak alinir 
    // ve "utf8" belirtilmez ise
    // ise asagidaki gibi buffer ciktisi verir
    // <Buffer 42 69 72 69 0d 0a 42 69 7a 69 0d 0a 47 6f 7a 65 74 6c 69 79 6f 72>
});

// DOsyaya Yazma Islemleri
fs.writeFile('dosya2.txt',"Kim seni gozetlesin amcik", function(hata){
    //belirtilen dosya bulunamaz ise olusturulur
    if(hata){
        throw hata;
    }

    console.log("Yazildi")
});

// write file dosya var ise uzerine yazar
//append file ise dosyaya ekleme yapar
fs.appendFile('dosya2.txt',"Kimmmmmm seni gozetlesin amcik", function(hata){
    if(hata){
        throw hata;
    }

    console.log("Yazildi")
});

// Dosya Silme
// DOsyaya Yazma Islemleri
//Asenkron calisir, diger fonksiyonlardan once calisir 
/*
fs.unlink('dosya2.txt', function(hata){
    if(hata){
        throw hata;
    }

    console.log("Silindi")
});

*/