// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueRouter from 'vue-router'
import router from './router'
import ElementUI from 'element-ui'
import lang from 'element-ui/lib/locale/lang/ja'
import locale from 'element-ui/lib/locale'
import 'element-ui/lib/theme-chalk/index.css'
import DataTables from 'vue-data-tables'

import App from './App'
// import 'font-awesome/css/font-awesome.min.css'

Vue.config.productionTip = false

Vue.use(ElementUI, {size: 'small'})
Vue.use(DataTables)
locale.use(lang)

Vue.use(VueRouter)

// For Training JavaScript
// main()
// For Training JavaScript

const route = new VueRouter(router)

route.beforeEach((to, from, next) => {
  document.title = to.meta.title
  next()
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<App/>',
  components: {App},
  router: route
})
