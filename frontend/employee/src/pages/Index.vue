<template>
  <div>
    <employee-header @changeMenu="changeMenu"></employee-header>
    <register v-if="this.menu === MenuIndex.Register"></register>
    <!--<search v-if="this.menuIndex === MenuIndex().Search"></search>-->
  </div>
</template>

<script>
  import Search from '@/pages/Search.vue'
  import Register from '@/pages/Register.vue'
  import EmployeeHeader from '@/components/EmployeeHeader.vue'
  import {
    MenuIndex
  }
  from '@/js/constants.js'

  export default {
    name: 'index',
    data () {
      return {
        menu: MenuIndex.Search
      }
    },
    methods: {
      changeMenu: function (index) {
        this.menu = index
      }
    },
    mixins: {
      MenuIndex
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
