// day 15

// level 1

class Animal {

    constructor (name, age, color, legs) {
        this.name = name
        this.age = age
        this.color = color
        this.legs = legs
    }
}

// level 2

class Dog extends Animal {

    constructor (name, age, color, legs, breed) {
        super(name, age, color, legs)
        this.breed = breed
    }
}

class Cat extends Animal {

}

// level 3

class PersonAccount {

    constructor(firstName, lastName) {
        this.firstName = firstName
        this.lastName = lastName
        this.incomes = new Map()    // description -> amount
        this.expenses = new Map()   // description -> amount
    }

    totalIncome() {
        let total = 0
        for (const amount of this.incomes.values()) {
            total += amount
        }
        return total
    }

    totalExpense() {
        let total = 0
        for (const amount of this.expenses.values()) {
            total += amount
        }
        return total
    }

    accountInfo() {
        console.log(`${this.firstName} ${this.lastName}`)
        console.log(`Total income: ${this.totalIncome()}`)
        console.log(`Total expenses: ${this.totalExpense()}`)
        console.log(`Balance: ${this.accountBalance()}`)
    }

    addIncome(income, description) {
        this.incomes.set(description, income)
    }

    addExpense(expense, description) {
        this.expenses.set(description, expense)
    }

    accountBalance() {
        return this.totalIncome() - this.totalExpense()
    }
}

const acct = new PersonAccount("Max", "Sun")
acct.addIncome(3000, "salary")
acct.addIncome(500, "freelance")
acct.addExpense(1200, "rent")
acct.accountInfo()