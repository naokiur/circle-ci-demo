<template>
  <div>
    <section>
      <el-container>
        <el-aside width="25rem">
          <div class="condition">
            <h3>条件</h3>
            <el-form ref="form" :model="form" label-position="left" label-width="4rem">
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
                <el-input-number :controls="false" v-model="age"></el-input-number>
              </el-form-item>
              <el-form-item label="入社年月日">
                <el-col :span="21">
                  <el-date-picker type="daterange" range-separator="〜" v-model="enterDateFrom" size="mini" style="width: 100%"/>
                </el-col>
              </el-form-item>
              <el-button @click="search" round>
                検索
              </el-button>
            </el-form>
          </div>
        </el-aside>
        <el-main>
          <section class="result">
            <h3 style="text-align: left">検索結果</h3>
            <el-row>
              <el-table style="height: 70vh;"
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
                <el-table-column>
                  <template slot-scope="scope">
                    <el-button
                      @click="deleteRow(scope.$index, scope.row)"
                      type="text"
                      size="small">
                      削除
                    </el-button>
                  </template>
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
        postList: [],
        age: '',
        enterDateFrom: '',
        enterDateTo: '',
        result: []
      }
    },
    created () {
      this.postList = [
          {key: '1', value: '部署1'},
          {key: '2', value: '部署2'}
      ]
    },
    methods: {
      search: function () {
        this.result = [
          {firstName: 'test1'},
          {firstName: 'test2'}
        ]
      },
      deleteRow: function (index, row) {
        console.log(index)
        console.log(row)
      }
    }
  }
</script>

<style scoped>
  .el-aside {
    height: 90vh;
  }

  .condition {
    padding: 0.5rem 1rem;
    background-color: #DEDEDE;
    height: auto;
  }

  .condition >>> div {
    margin: 0;
  }

  .condition >>> * {
    font-size: 80%;
    height: 80%;
  }

  .condition >>> .el-button {
    background-color: #5794BC;
    color: #FFFFFF;
    height: 100%;
    width: 100%;
    margin-top: 1rem;
  }

  .el-main {
    padding: 0;
    height: 90vh;
  }

  .result {
    margin: 0 1rem;
  }

  .el-form {
    text-align: left;
  }
</style>
