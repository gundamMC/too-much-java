<template>
  <div>
    <SideBar/>
    <router-link to="/test">hello!</router-link>
    ====
    <router-view></router-view>
  </div>
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
