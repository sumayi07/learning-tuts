// day 5

// level 1

const itCompanies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
console.log(itCompanies.join(", ") + " are big IT companies")

if (itCompanies.indexOf("Meta") == -1) {
    console.log("not found")
} else {
    console.log("found")
}

for (let i = itCompanies.length - 1; i > -1; i--) {
    
    let company = itCompanies[i]
    let oCount = company.split("o").length - 1
    console.log(company.split("o"))
    
    if (oCount > 1) {
        itCompanies.splice(i, 1)
    }
}

console.log(itCompanies)
itCompanies.splice(0)
console.log(itCompanies)

// level 2

const shoppingCart = ['Milk', 'Coffee', 'Tea', 'Honey']

shoppingCart.unshift("Meat")
shoppingCart.push("Sugar")
shoppingCart[3] = "Green Tea"

console.log(shoppingCart)

let text =
"I love teaching and empowering people. I teach HTML, CSS, JS, React, Python."

let cleaned = text.replace(/[^\w\s]/g, "")
const words = cleaned.split(" ")

console.log(words)
console.log(words.length)
