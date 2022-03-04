let audi = {
    speed: 250,
    model: "Audi",
    weight: 2
}

let bmw = Object.create(audi)

Object.prototype.toString = function() {
    console.log("Object printed")
}

Object.prototype.consoleInfo = function () {
    console.log("Console printed")
}

Array.prototype.sort = function (param) {
    return param
}

let arr = [5, 7, 8, 3]

// за счёт прототипов мы можем видизменять стандартное поведение каких-либо
// методов, так и добавлять новые методы, которые будут доступны всем
// последующим методам программы
