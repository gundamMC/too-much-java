<template>
  <SideBar/>
</template>

<script>

import SideBar from './components/SideBar.vue';

export default {
  components: {
    SideBar
  },
  data () {
    return {
      isCollapse: true
    }
  },
}
</script>
