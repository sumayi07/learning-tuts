// day 4

// level 1

let age = prompt("Enter your age")

if (age > 17) {
    console.log("You are old enough to drive.")
} else {
    console.log("You are left with " + (18 - age) + " years left to drive.")
}

let a = 4
let b = 3

a > b
    ? console.log(a + " is greater than " + b)
    : console.log(b + " is greater than " + a)

// level 2

let day = prompt("What is the day today? ")
day = day.toLowerCase()

if (day == "saturday" || day == "sunday") {
    console.log(day.charAt(0).toUpperCase() + day.slice(1) + " is a weekend.")
} else {
    console.log(day.charAt(0).toUpperCase() + day.slice(1) + " is a working day.")
}

// level 3

let month = prompt("What is the month? ")
month = month.toLowerCase()

if (month == "february") {
    console.log(month.charAt(0).toUpperCase() + month.slice(1) + " has 28 days")
} else if (month == "april" || month == "june" || month == "september" || month == "november") {
    console.log(month.charAt(0).toUpperCase() + month.slice(1) + " has 30 days")
} else {
    console.log(month.charAt(0).toUpperCase() + month.slice(1) + " has 31 days")
}