<template>
  <div>
    <el-input type="text" v-model="userName" name="userName" placeholder="ユーザ名"></el-input>
    <el-input type="password" v-model="password" name="password" placeholder="パスワード"></el-input>
    <el-button @click="login">ログイン</el-button>
  </div>
</template>

<script>
  export default {
    name: 'login',
    data () {
      return {
        userName: '',
        password: ''
      }
    },
    methods: {
      login: function () {
        this.$router.push('menu')
      }
    }
  }
</script>

<style>

</style>
