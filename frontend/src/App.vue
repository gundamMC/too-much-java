<template>
  <el-container>
    <el-main style="margin-top: 60px;">
      <router-view></router-view>
    </el-main>
    <el-header style="position: fixed; width: 100%; top: 0; z-index: 1000">
      <NavMenu/>
    </el-header>
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
