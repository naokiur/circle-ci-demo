<template>
  <div>
    <employee-header></employee-header>
    <h1>メニュー</h1>
  </div>
</template>

<script>
  import EmployeeHeader from '@/components/EmployeeHeader.vue'

  export default {
    name: 'menu',
    data () {
      return {
        name: ''
      }
    },
    methods: {
    },
    components: {
      EmployeeHeader
    }
  }
</script>

<style>

</style>
