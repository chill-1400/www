let array = [45, true, 6.92, "Hello", 'R'];
let str = array.join(" %$% ");
console.log(str);
console.log(array);

array.splice(1, 1); //( с какого эл-та удаляем масс, сколько эл. удал-ть)

console.log(array);

array[1] = false;
array[2] = "Hello";
array[3] += " World";

array[array.length] = 5;

array.pop(); //позвл. удол. послед. элемент
array.push("Bob", "Alex", 1);  //позвл. доб. элемент в конец массива
array.shift(); //позвл. удол. 1-й элемент
array.unshift("Bob", "Alex", 1); //позвл. доб. элемент в начало  массива

// array.length = 5;
delete array[2];

console.log(array);

// console.log(array.length);
// console.log(array.pop());

let arr = new Array(45, true, 6.92, "Hello", 'R');
console.log(arr);

let matrix = [
  [56, "Hello"],
  [5],
  [8.9, true, false, 56]
];

matrix[2][1] = "World";
matrix[0][2] = 45;
console.log(matrix[0][1]);

str = "Hello, world, 5, 0, qwe";
let array_split = str.split(", ");

console.log(array_split);
