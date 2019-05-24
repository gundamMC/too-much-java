<template>
  <div>
    {{test}}
    Hello!
    <router-link to="test">go to test</router-link>
  </div>

</template>

<script>

export default {
  data () {
    return {
      test: 'This is index'
    }
  },
}
</script>
