// day 9

// level 1

const countries = ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

countries.forEach(country => console.log(country))
console.log(countries.map(country => country.toUpperCase()))
console.log(countries.filter(country => country.includes("land")))
console.log(countries.reduce((acc, country) => acc + ", " + country) + " are North European countries")

// level 2

const products = [
  { product: 'banana', price: 3 },
  { product: 'mango', price: 6 },
  { product: 'potato', price: 2 },
  { product: 'avocado', price: 8 },
  { product: 'coffee', price: 10 },
  { product: 'tea', price: 5 },
]

console.log(products.map(dict => dict["price"]).reduce((acc, num) => acc + num))
console.log(products.reduce((acc, dict) => acc + dict["price"], 0))
