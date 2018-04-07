<template>
  <div>
    <section class="TopTitle">
      <h2>社員管理システム</h2>
      <h3> - <span class="abbr">E</span>mployee <span class="abbr">M</span>anagement <span class="abbr">S</span>ystem - </h3>
    </section>
    <section class="loginArea">
      <el-input
        type="text"
        v-model="userId"
        name="userName"
        placeholder="ユーザID">
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
  import axios from 'axios'

  export default {
    name: 'login',
    data () {
      return {
        userId: '',
        password: ''
      }
    },
    methods: {
      login: function () {
        const url = `${process.env.API_ENDPOINT}/api/login`

        const sendData = {
          user_id: this.userId,
          password: this.password
        }

        axios.post(url, sendData, {}).then(res => {
          console.log(res)
        }).catch(res => {
          console.log(res)
        })

        const authorizedUserName = 'test'
        const authorizedPassword = 'test'

        if (this.userId === authorizedUserName && this.password === authorizedPassword) {
          this.$router.push('index')
        } else {
          console.log('login error')
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
