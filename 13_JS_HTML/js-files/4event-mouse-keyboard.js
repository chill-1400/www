<div class="main-div">
  <input type="text" class="input" placeholder="Впишите что-то">
  <div class="hint">Подсказка при наведении</div>
</div>


<textarea name="name" rows="8" cols="80" class="full-text"></textarea>

<p>Lorem ipsum dolor <b class="bold-txt">sit amet</b>, consectetur adipisicing elit. Iusto, eaque.</p>




.main-div {
  position: relative;
}

.input {
  padding: 20px 15px;
  background: #fcfcfc;
  border-radius: 5px;
  border: 1px solid silver;
  outline: none;
  display: block;
  margin-bottom: 20px;
  width: 300px;
}

.hint {
  display: none;
  position: absolute;
  background: #fcfcfc;
  border-radius: 10px;
  border: 2px solid silver;
  padding: 10px;
}




let text = document.querySelector(".full-text");

text.onkeypress = function(e) {
  console.log("onkeypress: " + text.value);
};

text.onkeydown = function(e) {
  console.log("onkeydown: " + text.value);
};

text.onkeyup = function(e) {
  console.log("onkeyup: " + text.value);
};

let boldText = document.querySelector("p > b.bold-txt");

boldText.onmousedown = function() {
  boldText.style.color = "red";
};

boldText.onmouseup = function() {
  boldText.style.color = "blue";
};

boldText.oncontextmenu = function() {
  boldText.style.color = "green";
};

let inputField = document.querySelector('.input');
let helpField = document.querySelector('.hint');

inputField.onmouseenter = function() {
  helpField.style.display = "block";
};

inputField.onmousemove = function(e) {
  helpField.style.left = e.pageX + "px";
  helpField.style.top = e.pageY + "px";
};

inputField.onmouseleave = function() {
  helpField.style.display = "none";
};
