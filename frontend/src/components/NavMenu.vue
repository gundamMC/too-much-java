<template>
    <div>
        <!--    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">-->
        <!--      <el-radio-button :label="false">expand</el-radio-button>-->
        <!--      <el-radio-button :label="true">collapse</el-radio-button>-->
        <!--    </el-radio-group>-->
        <el-menu :default-active=$route.fullPath  mode="horizontal" router>
            <el-menu-item index="/" class="logo">
                <el-image
                style="width: 40px; height: 40px; margin-bottom: 10%; margin-right: 10%"
                :src="logo"/>
                <span>Too Much Java</span>
            </el-menu-item>
            <el-menu-item index="/test">
                <i class="el-icon-menu"></i>
                <span slot="title">Dashboard</span>
            </el-menu-item>
            <el-submenu index="/course">
                <template slot="title">
                    <i class="el-icon-location"></i>
                    <span slot="title">Courses</span>
                </template>
                <el-menu-item v-for="course in courses" :key="course.id" :index="'/course/' + course.id">
                    {{course.name}}
                </el-menu-item >
            </el-submenu>
            <el-menu-item index="3" disabled>
                <i class="el-icon-document"></i>
                <span slot="title">Navigator Three</span>
            </el-menu-item>

            <el-menu-item v-if="!loggedIn" index="/register" class="dock-right">
                <span slot="title">Register</span>
            </el-menu-item>
            <el-menu-item v-if="!loggedIn" index="/login" class="dock-right">
                <i class="el-icon-user"></i>
                <span slot="title">Login</span>
            </el-menu-item>



            <el-menu-item v-if="loggedIn" index="/profile" class="dock-right">
                <i class="el-icon-user"></i>
                <span slot="title">gundamMC</span>
            </el-menu-item>

        </el-menu>
    </div>
</template>

<script>
    import logo from '../assets/logo.png';

    export default {
        name: "NavMenu",
        data() {
            return {
                isCollapse: true,
                courses: [],
                logo: logo,
            }
        },

        computed: {
            loggedIn() {
                return this.$store.getters.loggedIn;
            }
        },

        created() {
            this.$store.dispatch('inspectToken').then(
                () => {
                    if (this.$store.getters.loggedIn) {
                        this.$api
                            .get('course/')
                            .then(response => (this.courses = response.data));
                    }
                });

      }
    }
</script>

<style scoped>
    .logo{
      display:inline-block;
      vertical-align:middle;
    }

    .el-menu--horizontal > .el-menu-item.dock-right {
        float: right;
    }
</style>