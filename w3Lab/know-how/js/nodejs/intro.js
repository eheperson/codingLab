
var http = require('http')
var log = require('./log.js')
var sayHello = require('./exportsDemo.js')


http.createServer(function(request, response){
    console.log(request.url)
    if(request.url=="/admin"){
        response.writeHead(200,{'Content-Type': 'text/html'})
        response.write('<html><body><strong>Admin Sayfasi</strong></body></html>')
    }else if(request.url=="/"){
        response.writeHead(200,{'Content-Type': 'text/html'})
        response.write('<html><body><strong>Admin sayfasindan baska bir sayfadasiniz.</strong></body></html>')
    }else if(request.url=="/customers"){
        response.writeHead(200,{'Content-Type': 'application/json'})
        // Gonderdigimiz ifadenin js datasi degil de 
        // json datasi oldugunu belirtmek icin
        // asagidaki kullanim ile beraber JSON.stringfy kullanilir
        // response.write({name:'abdurrahman', lastName:'Borklu'})
        response.write(JSON.stringify({name:'abdurrahman', lastName:'Borklu'}))
    }
    //response.writeHead(200,{'Content-Type': 'text/html'})
    response.end('<html><body> </br> Sayfa Icerigi</body></html>')
}).listen(8080)


log.information('Sunucu yayina geti')
//console.log(city)
console.log(sayHello())


