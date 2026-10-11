// day 7

// skipping many exercises cause they aren't worth doing

// level 1

function fullName (firstName, lastName) {
    return firstName + " " + lastName
}

console.log(fullName("Max", "Sun"))

const BMI = (weight, height) => {

    let bmi = weight / (height * height)

    if (bmi < 18.5) {
        console.log("underweight")
    } else if (bmi < 25) {
        console.log("normal weight")
    } else if (bmi < 30) {
        console.log("over weight")
    } else {
        console.log("obese")
    }
}

BMI(65, 1.8)

const findMax = (num1, num2, num3) => {

    let max = num1

    if (num2 > max) {
        max = num2
    }

    if (num3 > max) {
        max = num3
    }

    return max
}

console.log(findMax(-1, 5, 100))

// level 2

const solveQuadEquation = (a, b, c) => {

    if (a == 0 || b ** 2 - 4 * a * c < 0) {
        return "no solution"
    }

    const soln = new Set()
    soln.add((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))
    soln.add((-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))
    return soln
}

console.log(solveQuadEquation(1, 1, 4))

const reverseArray = arr => {
    
    const res = []

    for (let i = 0; i < arr.length; i++) {
        res.unshift(arr[i])
    }

    return res
}

console.log(reverseArray([1,2,3,4,5]))

// level 3

function rgbColorGenerator() {

    const rgb = []

    for (let i = 0; i < 3; i++) {
        rgb.push(Math.floor(Math.random() * 256))
    }

    return rgb
}

console.log(rgbColorGenerator())