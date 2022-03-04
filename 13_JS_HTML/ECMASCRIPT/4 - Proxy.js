// Proxy and object
const car = {
    model: 'BMW',
    speed: 230,
    weight: 1.3
}

const prox = new Proxy(car, {
    get(target, prop) {
        if(prop === "model")
            console.log("Модель вам не узнать!")
        else
            return target[prop]
    },
    set(target, prop, value) {
        if(['color', 'height', 'width', 'speed'].indexOf(prop) !== -1)
            throw Error("Такое значение установить нельзя")

        console.log(`Попытка установить ${prop} со значением ${value}`)
        if(prop === "model" && value === "Audi")
            target[prop] = value
        else
            console.error("Такое установить нельзя!")
    },
    has(target, prop) {
        if(prop === 'color')
            return true
    },
    deleteProperty(target, p) {
        if(p !== 'model')
            delete target[p]
        else
            throw Error("Модель удалить нельзя!")
    }
})


// Proxy and functions
const carMove = () => 'yeap, we are moving'

const proxMove = new Proxy(carMove, {
    apply(target, thisArg, argArray) {
        return target().toUpperCase()
    }
})

console.log(proxMove())


// Proxy and computed values
const user = {
    first: 'John',
    last: 'Doe',
    age: 23
}

const person = new Proxy(user, {
    get(target, prop) {
        if(!(prop in target)) {
            return prop.split("_").map(function (part) {
                return target[part]
            }).join(' ')
        } else
            return target[prop]
    }
})

console.log(person.first_last_age)