<template>
  <section>
    <h1>ログインページ</h1>
    <section class="contents">
    <el-form ref="form" :model="form" label-width="6rem">
      <el-form-item label="ユーザ名">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="パスワード">
        <el-input type="password" v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button @click="submitForm('form')">ログイン</el-button>
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
      form: {
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
