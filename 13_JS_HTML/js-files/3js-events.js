<a href="#" ondragend="clickHref()" class="href">Нажми на меня</a>

<p onclick="clickText('p')">Текст</p>
<p onclick="clickText('a.href')">Текст 2</p>

<input type="text" onfocus="focusEvent()" onblur="focusEndEvent()" onmouseover="focusEvent()" onmouseout="focusEndEvent()">

<textarea name="name" rows="8" cols="80" class="full-text"></textarea>

<div class="block">
  Привет мир!
</div>



function clickHref() {
  alert('Привет всем');
  document.querySelector("a.href").style.color = "#333";
  document.querySelector("a.href").style.textDecoration = "none";
}

function clickText(selector) {
  document.querySelector(selector).style.backgroundColor = "#333";
  document.querySelector(selector).style.color = "#fff";
}

// ------------------

let input = document.querySelector("input");

function focusEvent() {
  input.style.backgroundColor = "#333";
  input.style.padding = "10px";
  input.style.border = "0";
}

function focusEndEvent() {
  input.style.backgroundColor = "#fff";
  input.style.padding = "0px";
  input.style.border = "1px solid silver";
}

input.onmouseover = function() {
  console.log('onmouseover');
};

window.onresize = function() {
  console.log('Изменение ширины или высоты');
};

window.onload = function() {
  console.log("Страница загрузилась");
};

window.onscroll = function() {
  console.log("Скролл мышкой");
};

document.querySelector(".full-text").oninput = function() {
  console.log('Вы что-то вводите в textarea');
};

// ------------------------------

let block = document.querySelector("div.block");

function handlerOver() {
  block.innerHTML = "Новый текст";
}

function handlerOut() {
  block.innerHTML = "Привет мир!";
}

block.addEventListener("mouseover", handlerOver);
block.addEventListener("mouseout", handlerOut);

block.removeEventListener("mouseout", handlerOut);
