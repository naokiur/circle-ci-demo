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
  objects()
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

  let name = 'kittens'
  if (name === 'puppies') {
    name += ' woof'
  } else if (name === 'kittens') {
    name += ' meow'
  } else {
    name += '!'
  }
  console.log(name)
  // loop
  const array = ['a', 'b', 'c']
  for (let value of array) {
    console.log(value)
  }
  let animal = {
    hand: 2,
    foot: 2,
    heart: 1
  }
  for (let property in animal) {
    console.log(property)
    console.log(animal[property]) // I can access value of property.
  }
  // short-circuit logic
  let o = {
    name: 'test o'
  }
  let u
  let n = o && o.name
  let n2 = u && u.name
  // let n3 = u.name // This will be TypeError, short-circuit can avoid this error.
  console.log('n is ' + n)
  console.log('n2 is ' + n2)
  // console.log(n3)
  let alreadyCached = 'Cached!'
  let notCached
  console.log(alreadyCached || (alreadyCached = 'Second cache'))
  console.log(notCached || (notCached = 'Second cache'))
  // Ternary operator (三項演算子)
  const age = 18
  console.log((age > 18) ? 'yes' : 'no')
  // Switch
  let action = 'eat'

  switch (action) {
    case 'draw':
      console.log('draw now!')
      break // In ESLint, Required break.
    case 'eat':
      console.log('eat now!')
      break
    default:
      console.log('nothing!')
  }
  switch (action) {
    case 'eat':
    case 'draw': // But, this is ok.
      console.log('eat and draw')
      break
    default:
      console.log('nothing')
  }
  let stringCondition = '4'
  switch (stringCondition) {
    case 4:
      console.log('match!')
      break
    default: // switch use '===' operator.
      console.log('not match!')
  }
}

const objects = function () {
  console.log('------ objects ------')
  let obj = {
    name: 'Carrot',
    _for: 'max',
    details: {
      color: 'orange',
      size: 12
    }
  }
  console.log('obj.name:' + obj.name)
  console.log('obj[\'name\']:' + obj['name'])
  console.log('obj.details.color:' + obj.details.color)
  console.log('obj[\'details\'][\'color\']:' + obj['details']['color'])

  // class
  class Polygon {
    constructor (height, width) {
      this.height = height
      this.width = width
    }
  }
  let p = new Polygon(12, 5)
  console.log(p.height)
  console.log(p.width)
}
