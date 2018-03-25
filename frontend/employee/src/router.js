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
      path: '/index',
      name: 'index',
      meta: {title: 'NEMS'},
      component: () => import(/* webpackChunkName: "index" */'./pages/Index.vue')
    }
  ]
}
