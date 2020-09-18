//log isimli bir modul yazdik
var  log = {
    information : function(info){
        console.log("Information : " + info)
    },
    fault : function(f){
        console.log("Fault : " + f)
    }
}

// yazdigimiz modulu modul olarak disariya aktardik
// response ve require islemlerinde log ismi ile olusturdugumuz
// modulun modul oldugunu belirtmek icin bunu yapmamiz lazim
module.exports = log