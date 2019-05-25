<template>
    <div style="text-align: center; margin: 0 20%">
        <el-row>
            <h1 style="font-size: 32px">{{course.name}}</h1>
            <h2>{{course.description}}</h2>
            <el-divider/>
        </el-row>
        <el-row>
<!--            <el-card v-for="unit in course.units" :key="unit.id">-->
<!--                <div slot="header">-->
<!--                    <span>{{unit.name}}</span>-->
<!--                </div>-->
<!--                <div>-->
<!--                    {{unit.description}}-->
<!--                </div>-->
<!--                <el-divider/>-->
<!--                <div style="margin-top: 10px">-->
<!--                    <i class="el-icon-caret-bottom"></i>-->
<!--                </div>-->

<!--            </el-card>-->

            <collapseCard v-for="unit in course.units" :key="unit.id">
                <div slot="header">
                    <h3>{{unit.name}}</h3>
                    <p>{{unit.description}}</p>
                </div>
                <div>
                    <el-row type="flex" align="middle">
                        <el-col :span="4" :offset="2" style="margin-top: 25px;">
                            <el-row style="height: 50px">Assignments</el-row>
                            <el-row style="height: 50px">Quizzes</el-row>
                            <el-row style="height: 50px">Notes</el-row>
                        </el-col>
                        <el-col :span="5">
                            <el-row><el-progress type="circle" :percentage="25" width="50" status="text"></el-progress></el-row>
                            <el-row><el-progress type="circle" :percentage="25" width="50" status="text"></el-progress></el-row>
                            <el-row><el-progress type="circle" :percentage="25" width="50" status="text"></el-progress></el-row>
                        </el-col>
                        <el-col :span="2">
                            <el-divider direction="vertical"></el-divider>
                        </el-col>
                        <el-col :span="11">
                            <el-row>Assignments</el-row>
                            <el-row>Quizzes</el-row>
                            <el-row>Notes</el-row>
                        </el-col>
                    </el-row>
                </div>
            </collapseCard>

        </el-row>
    </div>

</template>

<script>
    import axios from 'axios';
    import collapseCard from '../components/collapseCard.vue';

    export default {
        components: {
            collapseCard
        },
        data() {
            return {
                course: {}
            }
        },
        mounted() {
            axios
                .get(`/api/course/${this.$route.params.id}/`)
                .then(response => (this.course = response.data))
        }
    }
</script>

<style>
  .el-row {
    margin-bottom: 20px;
  }
    .el-divider--vertical {
        height: 150px;
    }
</style>