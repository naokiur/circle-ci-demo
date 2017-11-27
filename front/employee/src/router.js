// import HelloWorld from '@/components/HelloWorld'

export default {
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'login',
      meta: {title: 'ログイン'},
      component: () => import(/* webpackChunkName: "login" */'./pages/Login.vue')
    }
  ]
}
