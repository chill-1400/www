let obj = '{ "name": "Андрей", "state": "USA", "male": true, "friends": [0,1,2,3] }';
// трансформация джейсон обьекта в обычный обьект
obj = JSON.parse(obj);

let array = '[56, 7, 2, 89]';

array = JSON.parse(array);

console.log(obj.friends[1]);

var object = {
  name: "Андрей",
  "age": 45,
  "state": 'UA'
};

// трансформация обычного обьекта в джейсон обьект
let str = JSON.stringify(object, "", 5);
console.log(str);
