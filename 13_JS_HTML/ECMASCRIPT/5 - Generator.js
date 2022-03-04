// function* generator() {
//     for(let i = 1; i <= 5; i++)
//         yield i
// }
//
// let numbers = generator()

// console.log(numbers.next())

let obj = {
    generator() {
        let i = 0
        return {
            next() {
                return {value: ++i, done: false}
            }
        }
    }
}

let gen = obj.generator()