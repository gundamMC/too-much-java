<template>
  <div id="app">
    <img src="./assets/logo.png">
    <div>
      <p>
        If Element is successfully added to this project, you'll see an
        <code v-text="'<el-button>'"></code>
        below
      </p>
      <el-button>el-button</el-button>
    </div>

    <div>
      <h2>Submission:</h2>
      <el-row v-for="sub in submissions" :key="sub.id">
        <el-col :span="12">
            Sub {{ sub.id }} - Points: {{ sub.points }} / {{ sub.total_points }}
        </el-col>
        <el-col :span="12">
          <el-button @click="selected_sub = sub">Select</el-button>
        </el-col>
      </el-row>

      <el-button style="margin: 10px;" size="small" type="success" @click="createSubmission">Create new submission</el-button>

    </div>

    <submit v-if="selected_sub != null" :submission="selected_sub"/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>

    {{ submissions }}

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import submit from './components/Submit';
import axios from 'axios';

export default {
  components: {
    HelloWorld,
    submit
  },
  data () {
    return {
      submissions: [],
      selected_sub: null
    }
  },
  methods: {
    createSubmission () {
      axios
              .post('/api/submission/', {'points': 0, 'total_points': 5})
              .then(response => (this.submissions.push(response.data)))
    }
  },
  mounted () {
    axios
      .get('/api/submission/')
      .then(response => (this.submissions = response.data))
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
