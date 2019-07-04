<template>
    <div>
        <!--    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">-->
        <!--      <el-radio-button :label="false">expand</el-radio-button>-->
        <!--      <el-radio-button :label="true">collapse</el-radio-button>-->
        <!--    </el-radio-group>-->
        <el-menu router :default-openeds="['/course/' + course_id]" :default-active="$route.fullPath">
            <h2>{{course.name}}</h2>
            <el-menu-item :index="'/course/' + course_id + '/'">
                <span slot="title">Overview</span>
            </el-menu-item>
            <el-submenu :index="'/course/' + course_id + '/'">
                <template slot="title">
                    <!--                    <i class="el-icon-location"></i>-->
                    <span slot="title">Units</span>
                </template>
                <el-menu-item v-for="unit in course.units" :key="unit.id" :index="'/course/' + course_id + '/unit/' + unit.id">
                    {{unit.name}}
                </el-menu-item>
            </el-submenu>
        </el-menu>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        props: {
            course_id: String,
        },
        data() {
            return {
                isCollapse: true,
                course: {},
                c_id: this.course_id.toString()  // course_id
            }
        },
        created() {
            axios
                .get(`/api/course/${this.course_id}/`)
                .then(response => (this.course = response.data));
        }
    }

</script>

<style scoped>

</style>