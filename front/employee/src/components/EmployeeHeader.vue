<template>
  <div>
    <el-menu :default-active="activeIndex" mode="horizontal" class="el-menu-demo" @select="handleSelect">
      <el-menu-item index="1">登録</el-menu-item>
      <el-menu-item index="2">検索</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
  export default {
    name: 'header',
    data () {
      return {
        actionIndex: '1'
      }
    }
  }
</script>

<style scoped>

</style>
