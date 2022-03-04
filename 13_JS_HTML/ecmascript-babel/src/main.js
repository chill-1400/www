let num = 5
let some = "some 123"
console.log(`Variable: ${num + 5}, second var: ${some}`)

let arr_1 = [5, 6, 2]
let arr_2 = [5, 9, ...arr_1]

function some() {
  return "hello";
}

const mult = (a, b) => a ** b;

console.log(mult());

setTimeout(() => {
  console.log("some")
}, 500);
