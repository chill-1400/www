function getAttributes()
{
 var u = document.getElementById("link").href;
 alert('Значение атрибута href ссылки: '+u);
 var v = document.getElementById("link").hreflang;
 alert('Значение атрибута hreflang ссылки: '+v);
 var w = document.getElementById("link").rel;
  alert('Значение атрибута rel ссылки: '+w);
 var x = document.getElementById("link").target;
  alert('Значение target атрибута ссылки: '+x);
 var y = document.getElementById("link").type;
  alert('Значение атрибута type ссылки: '+y);
}


var img = new Image();

// направление и скорость.

img.src = 'http://desktopwallpapers.org.ua/pic/201304/1600x900/desktopwallpapers.org.ua-25957.jpg';
var CanvasXSize = 1470;
var CanvasYSize = 900;
var speed = 30; //lower is faster
var scale = 1.05;
var y = -4.5; //вертикальное смещение

//Main

var dx = 0.75;
var imgW;
var imgH;
var x = 0;
var clearX;
var clearY;
var ctx;

img.onload = function() {
    imgW = img.width*scale;
    imgH = img.height*scale;
    if (imgW > CanvasXSize) { x = CanvasXSize-imgW; } // изображение больше холста
    if (imgW > CanvasXSize) { clearX = imgW; } // изображение больше холста
    else { clearX = CanvasXSize; }
    if (imgH > CanvasYSize) { clearY = imgH; } // изображение больше холста
    else { clearY = CanvasYSize; }
    //Получить элемент холста
    ctx = document.getElementById('canvas').getContext('2d');
    //Установить частоту обновления
    return setInterval(draw, speed);
}

function draw() {
    // Очистить холст
    ctx.clearRect(0,0,clearX,clearY);
    //If image is <= Canvas Size
    if (imgW <= CanvasXSize) {
        //сбросить, начать сначала
        if (x > (CanvasXSize)) { x = 0; }
        //рисовать дополнительное изображение
        if (x > (CanvasXSize-imgW)) { ctx.drawImage(img,x-CanvasXSize+1,y,imgW,imgH); }
    }
    //If image is > Canvas Size
    else {
        //сбросить, начать сначала
        if (x > (CanvasXSize)) { x = CanvasXSize-imgW; }
        //нарисовать дополнительное изображение
        if (x > (CanvasXSize-imgW)) { ctx.drawImage(img,x-imgW+1,y,imgW,imgH); }
    }
    //нарисовать изображение
    ctx.drawImage(img,x,y,imgW,imgH);
    //сумма для перемещения
    x += dx;
}
