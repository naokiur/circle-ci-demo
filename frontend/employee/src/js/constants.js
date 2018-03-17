// export const
// export const func = function () {
//   return 'aaa'
// }
//
export const MenuIndex = {
  Register: Symbol(1),
  Search: Symbol(2)
}

export default {
  data () {
    return {
      MenuIndex
    }
  },
  methods: {
    foo: function () {
      console.log('hello const mixin!')
    }
  }
}
