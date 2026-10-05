// day 3

// level 1
console.log(typeof "10" == 10)
console.log(parseInt("9.8") == 10)

console.log(!!0)
console.log(!!"hi")

console.log(4 === 4)
console.log(4 == "4")
console.log(4 === "4")

const now = new Date()

console.log(now.getFullYear())
console.log(now.getUTCDate())

// level 2
let base = prompt("Enter base")
let height = prompt("Enter height")
console.log("The area of the triangle is " + base * height / 2)

console.log(now.getMonth() + "/" + now.getDate() + "/" + now.getFullYear() + " " + now.getHours() + ":" + now.getMinutes())
