<template>
  <section>
    <h1>ログインページ</h1>
    <section class="contents">
    <el-form ref="form" :model="loginForm" label-width="6rem">
      <el-form-item label="ユーザ名">
        <el-input v-model="loginForm.name"></el-input>
      </el-form-item>
      <el-form-item label="パスワード">
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

export default {
  name: 'Login',
  data () {
    return {
      loginForm: {
        name: '',
        password: ''
      }

    }
  },
  methods: {
    submitForm (formName) {
      console.dir(formName)
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
