<template>
  <section>
    <h1>ログインページ</h1>
    <section class="contents">
    <el-form :model="loginForm" :rules="rules" ref="loginForm" label-width="6rem">
      <el-form-item label="ユーザ名" prop="name">
        <el-input v-model="loginForm.name"></el-input>
      </el-form-item>
      <el-form-item label="パスワード" prop="password">
        <el-input type="password" v-model="loginForm.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button @click="submitForm('loginForm')">ログイン</el-button>
      </el-form-item>
    </el-form>
    </section>
  </section>
</template>

<script>
import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
  name: 'Login',
  data () {
    return {
      loginForm: {
        name: '',
        password: '',
        csrf: ''
      },
      rules: {
        name: [
          { required: true, message: 'Need to input username', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Need to input password', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      console.log(this.$refs[formName])
      this.$refs[formName].validate((valid) => {
        if (valid) {
          axios.post('http://localhost:8000/news/', {
            name: this.$refs[formName].name,
            password: this.$refs[formName].password
          })
            .then(response => {
              console.log(response.status)
              console.log(response.data)
            })
        } else {
          alert('error')
          return false
        }
      })
    }
  }
}

</script>

<style scoped>
  .contents {
    width: 20rem;
    margin:0 auto;
  }
</style>
