// day 8

// level 1

const dog = {

    name: "Nick",
    legs: 4,
    color: "gold",
    age: 12,

    bark() {
        return "woof, woof"
    }
}

console.log(dog.bark())

dog.breed = "golden retriever"
dog.getDogInfo = function() {
    return `name: ${dog.name}, color: ${dog.color}, age: ${dog.age}, breed: ${dog.breed}`
}

console.log(dog.getDogInfo())

// level 2

const users = {
  Alex: {
    email: 'alex@alex.com',
    skills: ['HTML', 'CSS', 'JavaScript'],
    age: 20,
    isLoggedIn: false,
    points: 30
  },
  Asab: {
    email: 'asab@asab.com',
    skills: ['HTML', 'CSS', 'JavaScript', 'Redux', 'MongoDB', 'Express', 'React', 'Node'],
    age: 25,
    isLoggedIn: false,
    points: 50
  },
  Brook: {
    email: 'daniel@daniel.com',
    skills: ['HTML', 'CSS', 'JavaScript', 'React', 'Redux'],
    age: 30,
    isLoggedIn: true,
    points: 50
  },
  Daniel: {
    email: 'daniel@alex.com',
    skills: ['HTML', 'CSS', 'JavaScript', 'Python'],
    age: 20,
    isLoggedIn: false,
    points: 40
  },
  John: {
    email: 'john@john.com',
    skills: ['HTML', 'CSS', 'JavaScript', 'React', 'Redux', 'Node.js'],
    age: 20,
    isLoggedIn: true,
    points: 50
  },
  Thomas: {
    email: 'thomas@thomas.com',
    skills: ['HTML', 'CSS', 'JavaScript', 'React'],
    age: 20,
    isLoggedIn: false,
    points: 40
  },
  Paul: {
    email: 'paul@paul.com',
    skills: ['HTML', 'CSS', 'JavaScript', 'MongoDB', 'Express', 'React', 'Node'],
    age: 20,
    isLoggedIn: false,
    points: 40
  }
}

let logged_count = 0
let greater_than_50_count = 0

for (const user of Object.values(users)) {

    console.log(user)

    if (user.isLoggedIn) {
        logged_count += 1
    }
    if (user.points >= 50) {
        greater_than_50_count += 1
    }
}

console.log(`Number of users logged in: ${logged_count}`)
console.log(`Number of users with more than 50 points: ${greater_than_50_count}`)

// level 3

const personAccount = {

    firstName: "Max",
    lastName: "Sun",
    incomes: [
        {description: "unemployed", income: 0},
        {description: "parent's money", income: 100}
    ],
    expenses: [
        {description: "food", expense: 100}
    ],

    totalIncome() {

        let total = 0

        for (const income of this.incomes) {
            total += income.income
        }

        return total
    },

    totalExpenses() {

        let total = 0

        for (const expense of this.expenses) {
            total += expense.expense
        }

        return total
    },

    accountInfo() {
        return `name: ${this.firstName} ${this.lastName}, incomes: ${JSON.stringify(this.incomes)}, expenses: ${JSON.stringify(this.expenses)}`
    },

    addIncome(description, income) {
        this.incomes.push({description, income})
    },

    addExpense(description, expense) {
        this.expenses.push(description, expense)
    },

    accountBalance() {
        return this.totalIncome() - this.totalExpenses()
    }
}

console.log(personAccount.totalIncome())
console.log(personAccount.accountInfo())