
var dots = [];
var dotsNum = 0;

var bgcolor;

var canvas;
var h1;
var btn1;
var slider1;
var slider2;
var input1;
var input2;
var p1;
var p2;
var p3;

var xRect = 100;
var yRect = 100;

var xRel = 50;

var xPos = 900;
var yPos = 140;

var show = false;

var para
var button1

var bdy

var stdBtn

var paragraphs

function setup(){

    canvas = createCanvas(200,200);

    canvas.position(xPos,yPos);

    canvas.mouseOver(overCanvas);
    canvas.mouseOut(outCanvas);
    canvas.mousePressed(canvasPress);

    bgcolor = color(200);

    h1 = createElement("h1", "Waiting.... Come, Just Click Me !");
    //h1.position(400,100);
    h1.mousePressed(randomThings);

    h1.style("background-color:#dfdfdf; font-size:40px;")

    btn1 = createButton("Click Me Bitch");
    btn1.position(xPos+50,yPos+230);
    //Callback example
    btn1.mousePressed(changeBackground);

    slider1 = createSlider(1,100,10);
    slider1.position(xPos+40,yPos+260);
    slider1.changed(fuckingMessage);

    input1 = createInput("Type Something");
    input1.position(xPos+20, yPos+290);

    p1 = createP();
    p1.position(xPos+30, yPos+320);

    p2 = createP("Hey! There is some magic here.");
    p2.position(xPos+30, yPos+350);
    p2.mouseOver(overPara);
    p2.mouseOut(outPara);

    slider2 = createSlider(1,200,10);
    slider2. position(xPos +425, yPos);
    slider2.input(restyle);

    input2 = createInput("");
    input2.position(xPos +400, yPos+30);
    input2.input(showText);

    p3 = createP("");
    p3.position(xPos +400, yPos+50);

    para = select("#godstuff")
    para.mouseOver(changeBg);
    para.mouseOut(rechangeBg);

    button1 = select("#button1")
    button1.mousePressed(button1Click);

    bdy = select("body")

    stdBtn = select("#standartBtn")
    stdBtn.position(400,350)
    stdBtn.style("height:200px; width:200px;")
    stdBtn.mousePressed(owShit)

    paragraphs = selectAll("p")
    for(let i = 0; i<paragraphs.length;i++){
        paragraphs[i].mouseOut(higlight);
        paragraphs[i].mouseOver(unhighlight);
    }
 
    
}

function draw(){

    //clear();
    background(bgcolor);
    fill(255,0,175);
    rect(xRect,yRect,50,50);

    fill(255,175,0);
    ellipse(100,100,slider1.value(),slider1.value());

    xRect += random(-5,5);
    yRect += random(-5,5);

    if(xRect>=200)
        xRect=200-50;
    if(xRect<=0)
        xRect = 0+50;
    if(yRect>=200)
        yRect=200-50;
    if(yRect<=0)
        yRect = 0+50;

    xRel += random(-1,1);
    h1.position(xRel,550);

    fill(255,0,0);
    text(input1.value(),10,20);

    p1.html(input1.value());

    for ( let i = 0; i<dotsNum;i++){

        fill(0,255,0);
        ellipse(dots[i].x, dots[i].y, 10,10);
    }
    
}
/*
function mousePressed(){
    h1.html("And Thats are Some Random Number :")
    createP("Random number : "+ random(1,100));
 
}
*/
function randomThings(){
    h1.html("Welldone! And Here Some Random Number :")
    createP("Random number : "+ random(1,100));   
    let r = random(255);
    let g = random(255);
    let b = random (255);

    r = int(r);
    g = int(g);
    b = int(b);
    console.log(r);
    h1.style("background-color: rgb(" + r + "," + g + "," +b + ");");

    r = random(255);
    g = random(255);
    b = random (255);

    r = int(r);
    g = int(g);
    b = int(b);
    console.log(r);
    h1.style("color: rgb(" + r + "," + g + "," +b + ");");

}
function changeBackground(){
    bgcolor = random(250);
}

function overPara(){
    p2.html("Hahahaha! Magic is does not exist stupit!");
}

function outPara(){
    p2.html("Hey! There is some magic here.");
}

function overCanvas(){
    p2.html("MOVE YOUR MOUSE FROM CANVAS BITCH!!!!");

    
}

function outCanvas(){
    p2.html("Hey! There is some magic here.");  
}

function canvasPress(){

    let xVal = mouseX;
    let yVal = mouseY;

    dots.push({x:xVal,y:yVal});
    dotsNum +=1;
}

function fuckingMessage(){
    createP("Don't Play With it Bro!");  
}

function showText(){
    p3.html(input2.value());
}

function restyle(){
    p3.style("font-size :"+ slider2.value() + "px");
}

function changeBg(){
    para.style("background-color :  #434343;");
}

function rechangeBg(){
    para.style("background-color :  #ffffff;");
}

function button1Click(){
    
    let r = random(255);
    let g = random(255);
    let b = random (255);

    r = int(r);
    g = int(g);
    b = int(b);

    bdy.style("background-color: rgb(" + r + "," + g + "," +b + ");");

}

function owShit(){
    var elements = selectAll("p")
    let r = random(255);
    let g = random(255);
    let b = random (255);

    r = int(r);
    g = int(g);
    b = int(b);

    for (let i =0; i<elements.length; i++){
        elements[i].style("color: rgb(" + r + "," + g + "," +b + ");");
    }
}

function higlight(){
    let v = select("#ehes")

    let r = random(255);
    let g = random(255);
    let b = random (255);

    r = int(r);
    g = int(g);
    b = int(b);

    v.style("color: rgb(" + r + "," + g + "," +b + ");");

    r = random(255);
    g = random(255);
    b = random (255);

    r = int(r);
    g = int(g);
    b = int(b);

    v.style("background-color: rgb(" + r + "," + g + "," +b + ");");
}

function unhighlight(){}