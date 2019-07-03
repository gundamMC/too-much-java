<template>
    <div>
        <!--    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">-->
        <!--      <el-radio-button :label="false">expand</el-radio-button>-->
        <!--      <el-radio-button :label="true">collapse</el-radio-button>-->
        <!--    </el-radio-group>-->
        <el-menu default-active="2" class="el-menu-vertical-demo" router="true">
            <div class="logo">
                <el-image
                style="width: 80px; height: 80px;"
                :src="logo"/>
                <h1>Too Much Java</h1>
                <el-divider></el-divider>
            </div>
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
            <el-menu-item index="4">
                <i class="el-icon-setting"></i>
                <span slot="title">Navigator Four</span>
            </el-menu-item>
        </el-menu>
    </div>
</template>

<script>
    import axios from 'axios';
    import logo from '../assets/logo.png';

    export default {
        name: "SideBar",
        data() {
            return {
                isCollapse: true,
                courses: [],
                logo: logo
            }
        },
      mounted () {
        axios
          .get('/api/course/')
          .then(response => (this.courses = response.data))
      }
    }
</script>

<style scoped>
    .el-menu-vertical-demo:not(.el-menu--collapse) {
        width: 200px;
        min-height: 400px;
    }
    .logo{
        text-align: center;
        width: 80%;
        margin: 10% auto;
    }
</style>