<template>
  <div>
    <section>
      <input type="text" class="inputData" v-model="inputData" placeholder="please enter some test!" />
    </section>
    <section>
      <input type="button" value="send" @click="send" />
    </section>
    <section>
      <input type="text" :value="result" />
    </section>
  </div>
</template>

<script>
  export default {
    name: 'testTarget',
    data () {
      return {
        inputData: '',
        result: 'before'
      }
    },
    methods: {
      send: function () {
        this.result = this.inputData
      }
    }
  }
</script>

<style scoped>

</style>
