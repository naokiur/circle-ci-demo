<template>
  <div id="app">
    <test-target></test-target>
  </div>
</template>

<script>
import TestTarget from '@/pages/TestTarget.vue'

export default {
  name: 'app',
  data () {
    return {
    }
  },
  components: {
    TestTarget
  }
}
</script>

<style>
  /* html {
    background-color: #cccccc;
  } */
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
