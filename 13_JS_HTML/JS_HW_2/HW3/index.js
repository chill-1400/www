//Список всех жирных элементов
var bold_Items;
window.onload = getBold_items();

// Собираем все теги <b>
function getBold_items()
{
  bold_Items = document.getElementsByTagName('b');
}
//переброр выделенных жирным шрифтом тегов и изменение цвета
function highlight()
{
   for (var i=0; i<bold_Items.length; i++)
   {
    bold_Items[i].style.color ="red";
    }
}
// При отводе выделенные слова становятся черными
function return_normal()
{
  for (var i=0; i<bold_Items.length; i++)
  {
       bold_Items[i].style.color ="black";
  }
}



var img = new Image();

// направление и скорость.

img.src = 'https://mdn.mozillademos.org/files/4553/Capitan_Meadows,_Yosemite_National_Park.jpg';
var CanvasXSize = 800;
var CanvasYSize = 200;
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
