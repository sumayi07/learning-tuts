// day 13

// level 1

const countries = [
  ['Finland', 'Helsinki'],
  ['Sweden', 'Stockholm'],
  ['Norway', 'Oslo']
]

const user = {
  name: 'Asabeneh',
  title: 'Programmer',
  country: 'Finland',
  city: 'Helsinki',
  age: 250
}

console.table(countries)
console.table(user)

console.group("Countries")
console.log(countries)
console.groupEnd()

console.group("User")
console.log(user)
console.groupEnd()

// level 2

console.assert(10 > 2 * 10)
console.warn("This is a warning")
console.error("This is an error")

// level 3

console.time("regular for loop")

for (let i = 0; i < countries.length; i++) {
    console.log(countries[i])
}

console.timeEnd("regular for loop")

console.time("for of loop")

for (const arr of countries) {
    console.log(arr)
}

console.timeEnd("for of loop")

console.time("for each loop")

countries.forEach ((arr) => {
    console.log(arr)
})

console.timeEnd("for each loop")