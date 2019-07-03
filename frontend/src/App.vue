<template>
  <el-container>
    <el-header style="position: fixed; width: 100%;">
      <SideBar/>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script>

import SideBar from './components/SideBar.vue';

export default {
  components: {
    SideBar
  },
  data () {
    return {
      // something: true
    }
  },
}
</script>
