var h1 = document.createElement("h1");
h1.innerHTML = "Calculator";

var div1 = document.createElement("div");
var p1 = document.createElement("p");
var p2 = document.createElement("p");

div1.appendChild(p1);
div1.appendChild(p2);

var div2 = document.createElement("div");
var btn1 = document.createElement("button");
var btn2 = document.createElement("button");
var btn3 = document.createElement("button");
var btn4 = document.createElement("button");
var btn5 = document.createElement("button");
var btn6 = document.createElement("button");
var btn7 = document.createElement("button");
var btn8 = document.createElement("button");
var btn9 = document.createElement("button");
var btn10 = document.createElement("button");
var btn11 = document.createElement("button");
var btn12 = document.createElement("button");
var btn13 = document.createElement("button");
var btn14 = document.createElement("button");
var btn15 = document.createElement("button");
var btn16 = document.createElement("button");
var btn17 = document.createElement("button");

btn1.innerHTML = "NL";
btn2.innerHTML = "/";
btn3.innerHTML = "*";
btn4.innerHTML = "-";
btn5.innerHTML = "7";
btn6.innerHTML = "8";
btn7.innerHTML = "9";
btn8.innerHTML = "4";
btn9.innerHTML = "5";
btn10.innerHTML = "6";
btn11.innerHTML = "1";
btn12.innerHTML = "2";
btn13.innerHTML = "3";
btn14.innerHTML = "0";
btn15.innerHTML = ".";
btn16.innerHTML = "+";
btn17.innerHTML = "En";

div2.appendChild(btn1);
div2.appendChild(btn2);
div2.appendChild(btn3);
div2.appendChild(btn4);
div2.appendChild(btn5);
div2.appendChild(btn6);
div2.appendChild(btn7);
div2.appendChild(btn8);
div2.appendChild(btn9);
div2.appendChild(btn10);
div2.appendChild(btn11);
div2.appendChild(btn12);
div2.appendChild(btn13);
div2.appendChild(btn14);
div2.appendChild(btn15);
div2.appendChild(btn16);
div2.appendChild(btn17);

var body = document.querySelector("body");
body.appendChild(h1);
body.appendChild(div1);
body.appendChild(div2);
