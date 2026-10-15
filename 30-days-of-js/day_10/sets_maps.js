// day 10

// level 1

const a = [4, 5, 8, 9]
const b = [3, 4, 5, 7]
const countries = ['Finland', 'Sweden', 'Norway']

const emptySet = new Set()
const numSet = new Set()

for (let i = 0; i < 11; i++) {
    numSet.add(i)
}

console.log(numSet)

numSet.delete(10)
console.log(numSet)

numSet.clear()
console.log(numSet)

const countryCharMap = new Map()

for (const country of countries) {
    countryCharMap.set(country, country.length)
}

console.log(countryCharMap)

// level 2

let c = [...a, ...b]
const aUnionB = new Set(c)

console.log(aUnionB)

B = new Set(b)
c = a.filter((num) => B.has(num))
const aIntersectB = new Set(c)

console.log(aIntersectB)
