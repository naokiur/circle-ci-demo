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
      path: '/search',
      name: 'search',
      meta: {title: '検索画面'},
      component: () => import(/* webpackChunkName: "menu" */'./pages/Search.vue')
    }
  ]
}
