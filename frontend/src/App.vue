<template>
  <el-container>
    <el-header style="position: fixed; width: 100%;">
      <NavMenu/>
    </el-header>
    <el-main style="margin-top: 60px;">
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script>

import NavMenu from './components/NavMenu.vue';

export default {
  components: {
    NavMenu
  },
  data () {
    return {
      // something: true
    }
  },
}
</script>
