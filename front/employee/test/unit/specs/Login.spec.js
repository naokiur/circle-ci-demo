import Vue from 'vue'
import Login from '@/pages/Login.vue'

describe('Login.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(Login)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('h1').textContent)
    .to.equal('ログイン')
  })
})
