/*
//Pop-up
window.onload=function(){
    alert("eheheh");
};

//Console output
console.log("eheheh");

*/

/************ V A R I A B L E S  ***********************/
var variable1 = 13;
console.log(variable1);
variable1 += 10;
console.log(variable1);

var array =["ehe1", "ehe2", "ehe3", "ehe4"];
array[4] = "ehe5";
//alert(array);
console.log(array);
console.log("Array Length : " + array.length);
array.push("ehe6");
console.log(array);
console.log("Array Length : " + array.length);


var stringvar = "enivicivokki";

console.log(variable1 + stringvar);

/************     L O O P S     ***********************/

for(var i = 0; i<10;i++){
    console.log("i value : " + i);
}

/*----------------------------------------------------*/

var i = 0;

while(i<100){
    console.log("i value : " + i);
    i += 10;
}

/*----------------------------------------------------*/

var primaryNumbers = [2, 3, 5, 7, 11, 13, 17, 19];

console.log("Primary Numbers : ");

for(var i = 0; i<primaryNumbers.length;i++){
    console.log("Element : ", primaryNumbers[i]);
}


/************ D E C I S I O N   ***********************/

var x = 3;
var y = 5;
var z = 7;
var t = 13;

if(x<y){
    console.log("x is smaller than y");
}
/*----------------------------------------------------*/

if(x<y && y<z){
    console.log("x is smaller than y and y is smaller than z");
}
/*----------------------------------------------------*/

if(2=="2" && 3<10){
    console.log("Hallelujah... Check The Code ");
}
/*----------------------------------------------------*/

if(!(x>t)){
    console.log("x is not bigger  than t");
}
/*----------------------------------------------------*/

if(x>z){
    console.log("X is Bigger");
}
else{
    console.log("Z is Bigger");
}
/*----------------------------------------------------*/
if(x>z){
    console.log("X is Bigger Than Z");
}
else if (x>y){
    console.log("X is Bigger Than Y");
}
else if (x>t){
    console.log("X is Bigger Than T");
}
else{
    console.log("X is Smallest Number");
}
/*----------------------------------------------------*/

var a = 5;

switch(a){
    case 0:
        console.log("A is '0'");
        break;
    case 1:
        console.log("A is '1'");
        break;
    case 2:
        console.log("A is '0'");
        break;
    default:
        console.log("A is Different !");
        break;
}
/************ F U C N T I O N S ***********************/

function testFcn1(){
    console.log("Ellooo dear suckers")
}

testFcn1();
/*----------------------------------------------------*/

function testFcn2(a, b, c){
    console.log(a+b+c);
}

testFcn2(3, 7, 13);

/*----------------------------------------------------*/

function testFcn3(a, b, c){
    return a+b+c;
}

var res = testFcn3(10,20,30);
console.log("Result : " + res);

/*----------------------------------------------------*/

function Person(name, sname, age){

    this.name = name;
    this.sname = sname;
    this.age = age;
    this.showInfo = function(){
        return "Name :" + this.name + "\nSurname :" + this.sname + "\nAge :" + this.age;
    }
}

var newPerson = new Person("Abdurrahman", "Borklu", 345);
console.log(newPerson.showInfo());

/************  D A T A   S T R U C T U R E S   *******/

var realMan ={
    name : "Dogu",
    surname : "Perincek",
    talent : "Defender Of Abdulhamit",
    skills : {
        slapping : "**",
        fighting : "*",
        running : "******",
    },

    info : function(){
        return "Name : " + this.name + "\n" + "Surname : " + this.surname
      + "\n" + "Talent : " + this.talent;
    }
}

console.log("Name : " + realMan.name);
console.log("Surname : " + realMan.surname);
console.log("Talent : " + realMan.talent);
console.log("Fighting Ability : " + realMan.skills.fighting);
console.log("Slapping Ability : " + realMan.skills.slapping);
console.log("Running Ability : " + realMan.skills.running);
console.log(realMan.info());

/*----------------------------------------------------*/

var employer = new Object();

employer.name = "gunter";
employer.sname = "enivicivokki";
employer.age = 345;
employer.infos =  function(){
    return this.name + ", " + this.sname + ", " + this.age; 
}

console.log(employer.name);
console.log(employer.sname);
console.log(employer.age);
console.log(employer.infos());

/*----------------------------------------------------*/



/************    E     V     E     N     T     S    ***********************/

function clickButton1(){
    alert("Well Done Mother Fucker :) 1");
}

function clickButton2(element){
    element.innerHTML = "Well Done Mother Fucker :) 3";
    element.style.color = "blue";
}

function clickButton3(){
    var element = document.getElementById("header1");
    element.style.color = "red";
    element.innerHTML = "WELL DONE MOTHER FUCKER :') 4 "
}

function mouseover1(){
    var element =  document.getElementById("header1");
    element.innerHTML = "E N I V I C I V O K K I E M A N";
}

function mouseout1(){
    var element =  document.getElementById("header1");
    element.innerHTML = " JavaScript Test Page";
}

function check(){
    var form = document.forms["form1"];
    var deger = form["name1"].value;

    if(deger == ""){
        alert("Please Fill It!");
        return false;
    }

    return true;
}


