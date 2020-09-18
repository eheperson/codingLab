
let pageCounter = 1;

// select empty div in html page
let animalContainer = document.getElementById("animal-info")

// select specific button element from html page
let btn = document.getElementById("btn");

// Event Listener for button
btn.addEventListener("click", function(){
    // url adres for requesting 
    let url = 'https://raw.githubusercontent.com/eheperson/codingLAb/master/jsLAb/ajaxjs/json/animals-' + pageCounter + '.json'

    // r : our request
    let r = new XMLHttpRequest();

    // GET  : receive, download data
    // POST : send, upload data 
    r.open('GET', url);

    r.onload = function(){
        // d : data
        // JSON.parse() : convert text data to json format
        let d = JSON.parse(r.responseText)
        renderHtml(d);
        pageCounter++;

        if(pageCounter>3){
            btn.classList.add("hide-me");
        }
    };

    r.send();
});

function renderHtml(data){
    let htmlString = "";

    for(i = 0; i<data.length; i++){
        htmlString +=  "<p>" + data[i].name + "is a " + data[i].species + "that likes to eat";

        for(ii = 0; ii < data[i].foods.likes.length; ii++){
            if(ii == 0){
                htmlString += data[i].foods.likes[ii];
            }else{
                htmlString += " and " + data[i].foods.likes[ii];
            }
        }

        htmlString += ' and dislikes ';

        for(ii = 0; ii < data[i].foods.dislikes.length; ii++){
            if(ii == 0){
                htmlString += data[i].foods.dislikes[ii];
            }else{
                htmlString += " and " + data[i].foods.dislikes[ii];
            }
        }

        htmlString += ".</p>"
    }  
    animalContainer.insertAdjacentHTML('beforeend', htmlString);
};




/*
var myCat = {
    "name": "hosaf",
    "species" : "cat",
    "favFood" : "olive"
}

console.log("Name : ", myCat["name"])
console.log("Species : ", myCat["species"])
console.log("Favorite Food : ", myCat["favFood"])


var myFavColors = ["blue", "green", "purple"];

console.log(myFavColors[0], " , ", myFavColors[1], " , ", myFavColors[2])


var thePets = [
    {
        "name": "tom",
        "species" : "cat",
        "favFood" : "fish"
    },
    {
        "name": "jerry",
        "species" : "cheese",
        "favFood" : "olive"
    }
]

console.log("Name : ", thePets[1].name, " -- ", "Favorite Food : ", thePets[1].favFood)
*/