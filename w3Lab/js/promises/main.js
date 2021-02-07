/*
    A promise in javascipt is just like a promise in real life
    what you do is you commit to something by saying I promise to do something for example
    I promise to make the best video on promises as I can and then that promise either has
    two results either that promise complated it is resolved or that promise is failed and
    it is rejected so if I give you the best video ever on promises then I would  resolve 
    my promise to do so but if I failed to give you the best video ever on promises then 
    that would be rejected because I was not able to complete that promise adn I've rejected it.

    Syntax of creating promise : 
        let p = new Promise((resolve, reject) =>{
            // put simple code here
            let a = 1+1 
            if(a==2){
                resolve("Success")
            } else{
                reject("Failed")
            }
        }) 

*/

let p = new Promise((resolve, reject) =>{
    // put simple code here
    let a = 1+1
    if(a==2){
        resolve("Success")
    } else{
        reject("Failed")
    }
}) 
//interacting promises
//then is going to be called when our promise resolves succesfully
//catch is going to be called if our promise is rejected or failed
p.then((message)=>{
    console.log('This is in the then : ' + message)
}).catch((message) => {
    console.log('This is in the catch : ' + message)
})


//----------------------------------------------------------------------------------

/*
    Callback functions called with eventlisteners.
    if any event is occured callback function will be called

*/
let testFcn = function(){
    console.log("That is test function for callbacks");
}

// setTimeout : for the functions will run after some time
setTimeout(testFcn, 3000);  //3000 ms

console.log("Ellooooo");

//Anonymous function with setTimeout
setTimeout(function(){
    console.log("Anonymous callback test function");
},7000)

//----------------------------------------------------------------------------------

document.querySelector("#btn").addEventListener("click", function(){
        console.log("Button is clicked");
});

// Arrow function example
document.querySelector("#btn").addEventListener("mouseover", () => console.log("Mouse On the button !!") );

//----------------------------------------------------------------------------------

let posts = [
    {
        "title" : "Title 1",
        "body" : "Body 1"
    },
    {
        "title" : "Title 2",
        "body" : "Body 2"
    }
]

function addPost( callback){

    setTimeout(function(){
        posts.push({ "title" : "Title 3", "body" : "Body 3"})
        callback();
    }, 5000);
}

function getAllPosts(){
    setTimeout(allPosts,3000);
}

function allPosts(){
    let output = "<ul>";
    posts.forEach(function(post){
        output += `<li>  ${post.title} - ${post.body} </li>`;
    })

    output += "</ul>";
    document.getElementById("out").innerHTML = output;

}

addPost(getAllPosts);

//addPost();
//getAllPosts();
//
//there a asynchronous situation here, and that situation causes an logical error
// The problem : allPosts runs before the addPost, so, we cannot see title 3 on the screen
// 
//  Solution : 
//      If we send getAllPost to the addPost as callback function, 
//      we could handle that logical error succesfully as seen on line 89 and 108
