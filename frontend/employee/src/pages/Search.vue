<template>
  <div>
    <section>
      <el-container style="margin: 0.5rem;">
        <el-aside class="condition" width="30rem">
          <h3>条件</h3>
          <el-form ref="form" :model="form" label-position="left" label-width="6rem">
            <el-form-item label="名前">
              <el-col :span="10">
                <el-input v-model="firstName"></el-input>
              </el-col>
              <el-col :span="10" style="margin-left: 0.5rem">
                <el-input v-model="lastName"></el-input>
              </el-col>
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
              <el-col :span="8">
                <el-date-picker type="date" v-model="enterDateFrom" style="width: 100%" />
              </el-col>
              <el-col :span="2" style="margin-left: 0.5rem">
                <span>〜</span>
              </el-col>
              <el-col :span="8">
                <el-date-picker type="date" v-model="enterDateTo" style="width: 100%" />
              </el-col>
            </el-form-item>
            <el-button style="width: 100%"
              @click="search" round>
              検索
            </el-button>
          </el-form>
        </el-aside>
        <el-main>
          <section class="result">
            <el-row>
              <el-table
                :data="result">
                <el-table-column
                  prop="userId"
                  label="ユーザID">
                </el-table-column>
                <el-table-column
                  prop="firstName"
                  label="名字">
                </el-table-column>
                <el-table-column
                  prop="lastName"
                  label="名前">
                </el-table-column>
                <el-table-column
                  prop="post"
                  label="部署">
                </el-table-column>
                <el-table-column
                  prop="age"
                  label="年齢">
                </el-table-column>
                <el-table-column
                  prop="enterDate"
                  label="入社年月日">
                </el-table-column>
              </el-table>
            </el-row>
          </section>
        </el-main>
      </el-container>
    </section>
  </div>
</template>

<script>
  export default {
    name: 'search',
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
    /*width: 50rem;*/
    padding: 0.5rem 1rem;
    /*border-bottom: 0.1rem #e6e6e6 solid;*/
    background-color: #DEDEDE;
  }

  /*.el-form-item label {*/
  /*width: 3rem;*/
  /*}*/

  .result {
    margin: 1rem;
  }

  .el-form {
    text-align: left;
  }

  /*not affected*/
  /*label {*/
    /*text-align: center;*/
    /*background-color: #880000;*/
    /*font-size: large;*/
  /*}*/

  /*.el-col {*/
    /*padding: 0;*/
    /*margin: 0.5rem;*/
  /*}*/
</style>
