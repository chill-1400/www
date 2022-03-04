<div id="content" class="some">
  <p class="txt">1</p>
  <p class="txt some">2</p>
  <p class="txt">3</p>
  <p class="txt">4</p>
  <span>5</span>
  <div>5</div>
</div>

<ul class="test">
  <li>1</li>
  <li>2</li>
  <li class="some-test">3 <span class="span-text" id="span-text">span-text</span></li>
  <li>4</li>
  <li>5</li>
</ul>

<input type="password" name="fname" class="some" value="Some">

// console.log(document.head);
// console.log(document.body.childNodes);

// for(var i = 0; i < document.body.childNodes.length; i++) {
//   console.log(document.body.childNodes[i]);
// }

// let content = document.getElementById("content");

// let elements = content.getElementsByTagName("*")[2];
// console.log(elements);

// for(var i = 0; i < elements.length; i++)
//   console.log(elements[i]);

// let el = document.getElementsByName("fname")[0].tagName;
// console.log(el);
//
// let allClasses = document.getElementsByClassName("some")[1];
// console.log(allClasses);
//
// let elements = document.querySelectorAll("ul.test > li");
// console.log(elements);


// let ulItems = document.querySelector("#span-text");
let ulItems = document.querySelectorAll(".span-text")[0];
let parentLi = ulItems.closest(".some-test");

let input = document.querySelector("input[type]");
if(input != null) {
  input.value = "Что-то новое";

  input.setAttribute("data-toggle", "some value");
  input.setAttribute("type", "text");

  if(input.hasAttribute("type"))
    alert(input.getAttribute("class"));

  input.className = "some new test";
  alert(input.className);

  //input.removeAttribute("class");
}

input.style.backgroundColor = "red";
input.style.color = "#fff";
input.style.border = "2px solid silver";
input.style.borderRadius = "5px";
input.style.padding = "15px 10px";
