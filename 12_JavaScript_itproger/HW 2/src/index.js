

const findMin = arr => {
  let min = Infinity;
  for (let i = 0; i < arr.length; i++) {
    if (Array.isArray(arr[i])) {
      let _min = findMin(arr[i]);
      min = min > _min ? _min : min;
    } else {
      min = min > arr[i] ? arr[i] : min;
    }
  }
  return min;
};


let x = new Array(
  new Array(20, 34, 2),
  new Array(9, 12, 18),
  new Array(3, 4, 5)
);

let y = new Array(
  new Array(28, 5, 5, 5, 1),
  new Array(-4, 1, -7),
  new Array(-3, 3, 0)
);

document.getElementById("app").innerHTML = `
x: ${findMin(x)}</br>
y: ${findMin(y)}
`;
