<template>
  <div>
    <section class="condition">
      <h2>新規登録</h2>
      <el-row>
        <el-col :span="20">
          <el-form label-width="8rem">
            <el-form-item label="名前">
              <el-row type="flex" :gutter="20">
                <el-col :span="12">
                  <el-input v-model="firstName"></el-input>
                </el-col>
                <el-col :span="12">
                  <el-input v-model="lastName"></el-input>
                </el-col>
              </el-row>
            </el-form-item>
            <el-form-item label="部署">
              <el-select v-model="selectedPost">
                <el-option
                  v-for="post in postList"
                  :value="post.value"
                  :key="post.key"
                  :label="post.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="年齢">
              <el-input-number v-model="age"></el-input-number>
            </el-form-item>
            <el-form-item label="入社年月日">
              <el-row type="flex" :gutter="20">
                <el-col :span="10">
                  <el-date-picker type="date" v-model="enterDateFrom"/>
                </el-col>
                <el-col :span="3">
                  <span>〜</span>
                </el-col>
                <el-col :span="10">
                  <el-date-picker type="date" v-model="enterDateTo"/>
                </el-col>
              </el-row>
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>
    </section>
  </div>
</template>

<script>
  export default {
    name: 'register',
    data () {
      return {
        firstName: '',
        lastName: '',
        selectedPost: '',
        postList: [
          {key: '1', value: '部署1'},
          {key: '2', value: '部署2'}
        ],
        age: '',
        enterDateFrom: '',
        enterDateTo: '',
        result: []
      }
    },
    methods: {
      search: function () {
        this.result = [
          {firstName: 'test1'},
          {firstName: 'test2'}
        ]
      }
    }
  }
</script>

<style scoped>
  .condition {
    /*width: 50rem;*/
    padding: 0.5rem 1rem;
    border-bottom: 0.1rem #e6e6e6 solid;
  }

  .el-form-item label {
    width: 3rem;
  }

  .el-col {
    padding: 0;
  }
</style>
