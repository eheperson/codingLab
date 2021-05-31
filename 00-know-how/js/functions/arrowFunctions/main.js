//------------------------------------------------------------------

function sum(a,b){
    return a+b;
};
// Converting above function to arrow function :

// if below code is used, everything after arrow will be returned
// let sum2 = (a,b) => a + b;

let sum2 = (a,b) => {
    return a + b;
}

//------------------------------------------------------------------

function isPositive(number){
    return number >= 0;
};
// Converting above function to arrow function :
let isPositive2 = number => 0

//------------------------------------------------------------------

function randomNumber(){
    return Math.random
}
// Converting above function to arrow function :
// mean of the empt brackets : the function doesn't takes any input
let randomNumber2 = () => Math.random

//------------------------------------------------------------------

document.addEventListener('click', function(){
    console.log("click");
});
// Converting above function to arrow function :
document.addEventListener('click', () => console.log("click") );

//------------------------------------------------------------------
//------------------------------------------------------------------
//
// LET'S MOVE FORWARD 

class Person{
    constructor(name){
        this.name = name;
    };

    printNameArrow(){
        setTimeout( () => {
            console.log('Arrow : ' + this.name)
        }, 2000)
    }

    printNameFunction(){
        setTimeout(function() {
            console.log('Function : ' + this.name)
        }, 3000)
    }
}

let person = new Person('bob');

person.printNameArrow()

// printNameFunction() does not print person name
// because when class function called outside of the class scope
// this keyword redefined at every calling
// in global scobe .this keyword cannot refer to class variable
// !! That is the main difference between the arrow function's and standard function's working styles
person.printNameFunction()

//Again that code below does not print anything
//Because of the .this keyword.
//.this keyword is used in global scope
console.log(this.name)