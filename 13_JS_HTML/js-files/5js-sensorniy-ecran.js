 <div id="tap"></div>


#tap {
  position: fixed;
  left: 0;
  top: 0;
  display: inline-block;
  width: 80px;
  height: 80px;
  background: #eee;
  border-radius: 50%;

  transition: all 200ms linear;
}





let tap = document.getElementById("tap");

window.addEventListener('touchstart', function(e) {
  tap.style.background = "#333";
});

window.addEventListener('touchmove', function(e) {
  tap.style.left = e.targetTouches[0].pageX + "px";
  tap.style.top = e.targetTouches[0].pageY + "px";
});

window.addEventListener('touchend', function(e) {
  tap.style.background = "#eee";
});
