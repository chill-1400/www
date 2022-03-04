function makeCar(name) {
    return function(model) {
        console.log(name + ". Модель автомобиля: " + model)
    }
}

let audi = makeCar("Audi")
audi("TT")
audi("R8")

let bmw = makeCar("BMW")
bmw("M5")
bmw("i8")

// function makeCar(name, model) {
//     return console.log(name + ". Модель автомобиля: " + model)
// }
//
// makeCar("Audi", "TT")
// makeCar("Audi", "R8")
//
// makeCar("BMW", "M5")
// makeCar("BMW", "i8")