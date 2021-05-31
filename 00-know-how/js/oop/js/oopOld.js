/**         
 *      BEFORE ES6
 * 
 * 
 *   *  !!! Javascript uses 'prototype' method co create object.
 *  Before ES6, there was 3 ways to define an object :
 * 
 *      - Object Literal method:
 * 
 *          Object literal method could create only 1 instance of object
 *          If we used object literal method to define an object, we canneot create another instances
 *          Objects that created with object literal method becomes main data of the object
 * 
 * 
 *      - Constructor Function Method :
 * 
 *          Functions could be used for define objects in JS.
 *          The function is defined then another instance of the object could be derived with new keyword.
 *          new keyword cold be used with constructors only, cannot create another example from 'object literal' with new keyword !!!!!!!!!!!!!!!!!!
 * 
 * ! Only 1 instance could be created with object literal method, but a lot of instances could be created with constructor method.
 * ! if we want derive a lot of instances of the object that is created via object create method, we should use ' Object.create '
 * 
 *      - new Object() Method : 
 *          
 *          Objects could be created via instance of the "Object"
 *          that method is same with object literal method
 * 
 *  CHECK END OF THE FILE FOR THE INFORMATION ABOUT PROTOTYPE                <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  !!!!
 * 
 */
console.log("----------")
console.log("oopOld.js ")
console.log("----------")

 // OBJECT LITERAL METHOD
function star(){
    console.log("That is star object")
}

 var Star = {
     alive = true,
     color = "Blue",
     mass = 0,
     info:star,
     speak : function(){
         console.log("enivicivokki")
     }
 };

 console.log(Star.alive)
 //console.log(Star["alive"])

// adding new property of method to xiting object
Object.defineProperty(Star, 'age', {value : 0})
Star.diameter = 0

//check to see if object got the property of method 
Star.hasOwnProperty("name") //This will return False
Star.hasOwnProperty("mass") //This will return True

/*
Listing specs and methods of object

for (var spec in Star){
	console.log(spec)
}

var specs = Objects.keys(Star)
*/

// Creating instances of Object that creates via object literal method
s1 = Object.create(Star)
s2 = Object.create(Star)
/**
 * If any instance being created via Object.create, that instance shall be same with main object.
 * Properties and methods of the derived object shall be same with main object.
 * This derived instance will be clone of the main object with same properties and methods
 */

 // If we wanna create instance with different properties
 var Star2 = Object.create({},
                            {
                                alive : {
                                    value:"undefined",
                                    writable:true,
                                    enumerable:true,
                                    configurable:true
                                },
                                color : {
                                    value:"undefined",
                                    writeble:true,
                                    enumerable:true,
                                    configurable:true
                                }
                            });

 // If we wanna create same instance with different properties         
 var s3 = Object.create(Star,
                        {
                            alive : {
                                value : true,
                                configurable: true,
                                writable:true,
                                enumerable:true
                            },
                            color : {
                                value : 'undefined',
                                configurable: true,
                                writable:true,
                                enumerable:true
                            },
                            mass : {
                                value : 0,
                                configurable: true,
                                writable:true,
                                enumerable:true
                            }
                        })                   


// CONSTRUCTOR METHOD

function creature(){
    species : "undefined";
}
/*
 creature = function(){
    species : "undefined";
}
*/

var c1 = new creature()
// var c1 = new creature
var c2 = new creature()
var c3 = new creature()
var c4 = new creature()
// !!! new parameter could be used with constructor method only !!!!!!!!!!!!!!!!!!!!!!!!!!!

// Constructor could take parameters also
function creatureV2(s, a){
    this.species = 2,
    this.age = a,
    this.info = function(){
        console.log("age : " + this.age + " species : " + this.species)
    }
};

/*  Object Literal version of above code

function i(){
    console.log("age : " + this.age + " species : " + this.species)
}

var creatureV2 = {
    species = 'unkown',
    age = 0
    info : i
}
*/

// OBJECT INSTANCE METHOD
var test = new Object()
// same as : var test = {}


/*
    In objects created with constructor method, have a property named 'prototype'
    'prototype' is an object and we could reach prototype informations of the objects via that property.

    We can use 'Object' keyword for  prototype, because prototype is an object also.

    function Test(name){
        this.name = name,
        this.speak = function(){
            cosole.log("eheheheheh")
        }
    }

    var t1 = new Test("gunter")

    -that code below adds a property to instance t1
    t1.sname = "notman"

    -we could add properties to the main objet with prototype keyword, not to the instance
    -that code below adds property to class(main object, not to instance)
    Test.property.sayHello = function(){
        console.log("ellooooooo")
    }

!!!!!!!!! 'prototype' property allows us to reach properties of class   !!!!!!!!!!!!!!!!!!

*/