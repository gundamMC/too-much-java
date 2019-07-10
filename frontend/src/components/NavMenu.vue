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
            <el-menu-item index="/test/">
                <i class="el-icon-menu"></i>
                <span slot="title">Dashboard</span>
            </el-menu-item>
            <el-submenu :disabled="!loggedIn" index="/course/">
                <template slot="title">
                    <i class="el-icon-document"></i>
                    <span slot="title">Courses</span>
                </template>
                <el-menu-item v-for="course in courses" :key="course.id" :index="'/course/' + course.id + '/'">
                    {{course.name}}
                </el-menu-item >
            </el-submenu>

            <el-menu-item v-if="!loggedIn" index="/register/" class="dock-right">
                <span slot="title">Register</span>
            </el-menu-item>
            <el-menu-item v-if="!loggedIn" index="/login/" class="dock-right">
                <i class="el-icon-user"></i>
                <span slot="title">Login</span>
            </el-menu-item>

            <el-submenu v-if="loggedIn" class="dock-right" index="/">
                <template slot="title">
                    <i class="el-icon-user"></i>
                    <span slot="title">{{user.username}}</span>
                </template>
                <el-menu-item @click="logout">
                    <span slot="title">Logout</span>
                </el-menu-item >
            </el-submenu>

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
                logo: logo,
            }
        },

        computed: {
            loggedIn() {
                return this.$store.getters.loggedIn;
            },
            courses() {
                return this.$store.getters.courses;
            },
            user() {
                return this.$store.getters.user;
            }
        },

        created() {
            this.$store.dispatch('inspectToken');

      },

        methods: {
            logout() {
                this.$store.commit('removeToken');
                this.$store.commit('removeCourseList');
                this.$store.commit('removeUser');
                this.$router.push('/');
            }
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

    .el-menu--horizontal > .el-submenu.dock-right {
        float: right;
    }
</style>