
export default {
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      meta: {title: 'Login'},
      component: () => import(/* webpackChunkName: "hello" */'./pages/Login.vue')
    }
  ]
}
