<template>
  <div id="app">
    <login></login>
  </div>
</template>

<script>
import Login from '@/pages/Login.vue'

export default {
  name: 'app',
  data () {
    return {
    }
  },
  components: {
    Login
  }
}
</script>

<style>
  html {
    background-color: #cccccc;
  }
  body {
    margin: 0;
  }
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    text-align: center;
    color: #2c3e50;
    /*margin-top: 2rem;*/
    margin: 0;
  }
</style>
