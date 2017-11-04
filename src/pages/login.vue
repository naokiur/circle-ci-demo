<template>
  <section>
    <h1>ログインページ</h1>
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="User name">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="Password">
        <el-input type="password" v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button @click="submitForm('form')">ログイン</el-button>
      </el-form-item>
    </el-form>
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

</style>
