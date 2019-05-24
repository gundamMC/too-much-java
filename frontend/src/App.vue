<template>
  <el-container>
    <el-aside>
      <SideBar/>
    </el-aside>
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
