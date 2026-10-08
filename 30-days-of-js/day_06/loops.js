// day 6

// I'm skipping a lot of the exercises because they just aren't worth doing

// level 1

console.log("i" + "\t" + "i^2" + "\t" + "i^3")

for (let i = 0; i < 11; i++) {
    console.log(i + "\t" + i * i + "\t" + i * i * i)
}

let uniqueNums = []

while (uniqueNums.length < 5) {

    let i = Math.floor(Math.random() * 10)

    if (uniqueNums.indexOf(i) == -1) {
        uniqueNums.push(i)
    }
}

console.log(uniqueNums)

// level 2

let hexdec = "abcdef0123456789"
let hexdecID = "#"

while (hexdecID.length < 7) {
    hexdecID += (hexdec.charAt(Math.floor(Math.random() * hexdec.length)))
}

console.log(hexdecID)

let countries = ["ALBANIA", "BOLIVIA", "CANADA", "DENMARK", "ETHIOPIA", "FINLAND", "GERMANY", "HUNGARY", "IRELAND", "JAPAN", "KENYA"]
let subset = []

for (const country of countries) {

    if (country.lastIndexOf("IA") == country.length - 2) {
        subset.push(country)
    }
}

console.log(subset)