
export default {
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Hello',
      meta: {title: 'Hello'},
      component: () => import(/* webpackChunkName: "hello" */'./components/Hello.vue')
    }
  ]
}
