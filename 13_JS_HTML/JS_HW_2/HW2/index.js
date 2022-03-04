function getSize()
{
var w = document.documentElement.clientWidth;
var h = document.documentElement.clientHeight;

// put the result into a h1 tag
 document.getElementById('wh').innerHTML ="<h1>Ширина: " + w + "px <br>Высота: " + h + "px </h1>";
}

let block = document.querySelector("div.block");

function handlerOver() {
  block.innerHTML = "<h1>Мини веб сайт</h1>";
}

block.addEventListener("mouseover", handlerOver);
