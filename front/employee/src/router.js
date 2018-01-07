export default {
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'login',
      meta: {title: 'ログイン'},
      component: () => import(/* webpackChunkName: "login" */'./pages/Login.vue')
    },
    {
      path: '/menu',
      name: 'menu',
      meta: {title: 'メニュー'},
      component: () => import(/* webpackChunkName: "menu" */'./pages/Menu.vue')
    }
  ]
}
