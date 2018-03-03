<template>
  <div>
    <section class="loginArea">
      <el-input
        type="text"
        v-model="userName"
        name="userName"
        placeholder="ユーザ名">
      </el-input>
      <el-input
        type="password"
        v-model="password"
        name="password"
        placeholder="パスワード">
      </el-input>
      <el-button @click="login">ログイン</el-button>
    </section>
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
        const authorizedUserName = 'test'
        const authorizedPassword = 'test'

        if (this.userName === authorizedUserName && this.userName === authorizedPassword) {
          this.$router.push('index')
        }
      }
    }
  }
</script>

<style scoped>
  .loginArea {
    width: 25rem;
    margin: auto;
  }


</style>
