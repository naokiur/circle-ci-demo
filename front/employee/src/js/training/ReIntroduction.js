export default function () {
  console.log('This is main for training JavaScript')
  otherFunc()
  callSubjects()
}

const callSubjects = function () {
  console.log('----- begin subjects -----')
  types()
  operators()
  controlStructure()
  console.log('----- end subjects -----')
}

const otherFunc = function () {
  console.log('other Func!!')
}

export const secondFunction = function () {
  console.log('Second function!!')
}

const types = function () {
  console.log('------ begin type ------')
  // Number
  console.log(0.1 + 0.2)
  const stringNumber = '012'
  console.log(parseInt(stringNumber, 10))
  let count = 2
  console.log(count + '010') // cannot add but can concat.
  // String
  const word = 'hello'
  console.log(word.length)
  console.log(word.charAt(2))
  console.log(word.replace('ll', 'rr'))
  console.log(word.toUpperCase())
  // Boolean
  const falseFromfalse = Boolean(false)
  // const falseFromString = Boolean('false') // This is true
  const falseFrom0 = Boolean(0)
  const falseFromEmpty = Boolean('')
  const falseFromNaN = Boolean(NaN)
  const falseFromNull = Boolean(null)
  const falseFromUndef = Boolean(undefined)
  console.log(falseFromfalse)
  // console.log(falseFromString)
  console.log(falseFrom0)
  console.log(falseFromEmpty)
  console.log(falseFromNaN)
  console.log(falseFromNull)
  console.log(falseFromUndef)
}

const operators = function () {
  console.log('------ begin operators ------')

  let x = 5
  console.log(x)
  x += 5
  console.log(x)
  console.log('hello' + ' world') // hello world
  console.log(3 + 4 + 5)
  console.log('3' + 4 + 5)
  console.log(3 + 4 + '5')
  console.log(123 === '123') // false
  console.log(1 === true) // false
}

const controlStructure = function () {
  console.log('------ controlStructure ------')
}
