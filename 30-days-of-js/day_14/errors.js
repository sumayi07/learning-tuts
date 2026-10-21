// day 14

try {
  let lastName = 'Yetayeh'
  let fullName = fistName + ' ' + lastName
} catch (err) {
  console.log('Name of the error', err.name)
  console.log('Error message', err.message)
} finally {
  console.log('In any case I will be executed')
}

// const throwErrorExampleFun = () => {

//   let x = prompt('Enter a number: ')
//   try {
//     if (x == '') throw 'empty'
//     if (isNaN(x)) throw 'not a number'
//     x = Number(x)
//     if (x < 5) throw 'too low'
//     if (x > 10) throw 'too high'
//   } catch (err) {
//     console.log(err)
//   }
// }
// throwErrorExampleFun()