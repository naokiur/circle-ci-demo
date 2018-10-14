<template>
  <div>
    <section>
      <el-row justify="center" type="flex">
        <el-col :span="12">
          <el-row class="employeeInformarion" justify="center" type="flex">
            <el-col>
              <h2>新規登録</h2>
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
                  <el-input-number size="mini" :controls="false" v-model="age" :min="0"></el-input-number>
                </el-form-item>
                <el-form-item label="入社年月日">
                  <el-row type="flex" :gutter="20">
                    <el-col :span="10">
                      <el-date-picker type="date" v-model="enterDate"/>
                    </el-col>
                  </el-row>
                </el-form-item>
                <el-button @click="register" round>
                  登録
                </el-button>
              </el-form>
            </el-col>
          </el-row>
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
        enterDate: ''
      }
    },
    methods: {
      register: function () {
        const storage = sessionStorage

        const user = {
          firstName: this.firstName,
          lastName: this.lastName,
          post: this.selectedPost,
          age: this.age,
          enterDate: this.enterDate
        }

        if (storage['userList'] === undefined) {
          storage['userList'] = JSON.stringify([user])
        } else {
          const userList = JSON.parse(storage['userList'])
          userList.push(user)
          storage['userList'] = JSON.stringify(userList)
        }
      }
    }
  }
</script>

<style scoped>
  .employeeInformarion {
    width: 50%;
    padding: 0.5rem 1rem;
    /* margin: auto; */
    border-bottom: 0.1rem #e6e6e6 solid;
    background-color: #FFFFFF;
  }

  .el-form-item label {
    width: 3rem;
  }

  .el-col {
    padding: 0;
  }
</style>
