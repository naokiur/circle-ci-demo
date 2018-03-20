<template>
  <div>
    <h2 style="text-align: left; margin: 0 0 0.5rem 0.5rem">社員管理システム（EMS）</h2>
    <el-menu :default-active="activeIndex" mode="horizontal" class="el-menu-demo">
      <el-menu-item index="1" @click="changeMenu(MenuIndex.Register)">登録</el-menu-item>
      <el-menu-item index="2" @click="changeMenu(MenuIndex.Search)">検索</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
  import constants from '@/js/constants'

  export default {
    name: 'header',
    data () {
      return {
        activeIndex: '2'
      }
    },
    // props: {
    //   activeIndex: 2
    // },
    mixins: [constants],
    methods: {
      changeMenu: function (index) {
        this.$emit('changeMenu', index)
      }
    }
  }
</script>

<style scoped>

</style>
