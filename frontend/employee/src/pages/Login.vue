<template>
  <div>
    <section class="TopTitle">
      <h2>社員管理システム</h2>
      <h3> - <span class="abbr">E</span>mployee <span class="abbr">M</span>anagement <span class="abbr">S</span>ystem - </h3>
    </section>
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
  .TopTitle {
    background-color: #5794BC;
    color: #FFFFFF;
    margin: 1rem 10rem;
  }

  .loginArea {
    width: 25rem;
    margin: auto;
  }

  .abbr {
    color: #FFD04B;
  }


</style>
