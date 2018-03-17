<template>
  <div>
    <employee-header @changeMenu="changeMenu"></employee-header>
    <register v-if="this.menu === MenuIndex.Register"></register>
    <search v-if="this.menu === MenuIndex.Search"></search>
  </div>
</template>

<script>
  import Search from '@/pages/Search.vue'
  import Register from '@/pages/Register.vue'
  import EmployeeHeader from '@/components/EmployeeHeader.vue'
  import constants from '@/js/constants'

  export default {
    name: 'index',
    mixins: [constants],
    data () {
      return {
        menu: ''
      }
    },
    methods: {
      changeMenu: function (index) {
        this.menu = index
      }
    },
    created () {
      this.foo()
    },
    components: {
      EmployeeHeader,
      Register,
      Search
    }
  }
</script>

<style scoped>

</style>
