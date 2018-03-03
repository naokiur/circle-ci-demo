<template>
  <div>
    <employee-header></employee-header>
  </div>
</template>

<script>
  import Search from '@/pages/Search.vue'
  import EmployeeHeader from '@/components/EmployeeHeader.vue'

  export default {
    name: 'index',
    components: {
      EmployeeHeader,
      Search
    }
  }
</script>

<style scoped>

</style>
