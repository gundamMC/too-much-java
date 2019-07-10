<template>
    <div style="text-align: center">
          <div style="margin-top: 10%">
            <h1 style="font-size: 72px">Too Much Java</h1>
            <h2>An automatic code grading platform</h2>
          </div>
        <div style="margin-top: 100px">
            <h1>Deployed at</h1>
            <h1 style="font-size: 24px">{{host}}</h1>
          </div>

        <div class="footer">
            <el-divider></el-divider>
            <p>
                By <a href="https://gundammc.com">gundamMC</a>,
            open sourced on <a href="https://github.com/gundamMC/too-much-java">Github</a>
            </p>
            <div style="margin-top: 10px">  <!-- badges -->
                <el-image src="https://forthebadge.com/images/badges/made-with-vue.svg"></el-image>
                <el-image src="https://forthebadge.com/images/badges/powered-by-electricity.svg"></el-image>
                <el-image src="https://forthebadge.com/images/badges/gluten-free.svg"></el-image>
                <el-image src="https://forthebadge.com/images/badges/winter-is-coming.svg"></el-image>
            </div>
        </div>
    </div>


</template>

<script>

    import settings from '../settings';

export default {
  data () {
    return {
        host: settings.host
    }
  },
}
</script>

<style scoped>
    .footer {
        bottom: 0;
        left: 0;
        position: fixed;
        padding: 10px 0;
        width: 100%;
        text-align: center;
    }

    .el-image {
        margin: 0 10px;
    }

</style>