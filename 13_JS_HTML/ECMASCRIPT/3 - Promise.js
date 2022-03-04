// Simple example of Promise
let p = new Promise(function(resolve, reject) {
    let isGoodVideo = false
    if(isGoodVideo) {
        resolve("Video is nice")
    } else {
        reject('Video is failed')
    }
})

p.then((mess) => {
    console.log("Mess: " + mess)
}).catch((mess) => {
    console.log("Mess: " + mess)
})


// Example of Callback with Promise
let jsBetterThanPhp = true
let nodeJsIsGreat = false

function isJsWorthCallback() {
    return new Promise((resolve, reject) => {
        if(jsBetterThanPhp && nodeJsIsGreat) {
            resolve({
                isWorth: true,
                name: "JS"
            })
        } else
            reject("JS isn't so great :(")
    })
}

isJsWorthCallback().then((mess) => {
    console.log("Success: " + mess.name)
}).then(() => {
    console.log("Next message")
}).catch((error) => {
    console.error("Err: " + error)
}).finally(() => {
    console.warn("All is done!")
})



// Promise All
const p1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log('Starting')
        resolve()
    }, 1000)
})

const p2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log('Fetching Data')
        resolve()
    }, 2000)
})

const p3 = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log('Finish')
        resolve()
    }, 3000)
})

Promise.all([p1, p2, p3]).then(() => {
    console.log("App finished")
}).catch(() => {
    console.error("Error")
})


// Fetch Data
fetch('https://reqres.in/api/users')
    .then(res => res.json())
    .then((data) => {
        console.log(data)
        console.log(data.data[2].email)
    })