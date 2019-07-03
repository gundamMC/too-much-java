<template>
    <div style="text-align: center; margin: 0 20%">
        <el-row>
            <h1 style="font-size: 32px">{{unit.name}}</h1>
            <h2>{{unit.description}}</h2>
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

            <!--            <div style="height: 300px;">-->
            <!--              <el-steps direction="vertical" :active="1" reverse>-->
            <!--                <el-step title="Step 1" icon="el-icon-document" time></el-step>-->
            <!--                <el-step title="Quiz: Java Basics" icon="el-icon-menu"></el-step>-->
            <!--                <el-step title="Note #1" icon="el-icon-notebook-2"></el-step>-->
            <!--              </el-steps>-->
            <!--            </div>-->

            <div class="block">
                <el-timeline style="text-align: left; margin: 0 20%">
                    <el-timeline-item v-for="assignment in unit.assignments" :key="assignment.id" :timestamp="assignment.date" placement="top">
                        <el-card shadow="hover">
                            <div slot="header">
                                <i class="el-icon-menu"></i>
                                <span>    {{assignment.name}}</span>
                            </div>
                            <p>{{assignment.description}}</p>
                            <p class="small-font">Due: {{assignment.due_date}}</p>
                        </el-card>
                    </el-timeline-item>
                </el-timeline>
            </div>

        </el-row>
    </div>

</template>

<script>
    import axios from 'axios';
    import moment from 'moment';

    export default {
        components: {},
        data() {
            return {
                unit: {},
                bg_style: {
                    backgroundColor: "#fafafa"
                }
            }
        },
        created() {
            axios
                .get(`/api/unit/${this.$route.params.id}/`)
                .then(response => {

                    for(let i = 0; i < response.data.assignments.length; i++){
                        response.data.assignments[i].date = moment(response.data.assignments[i].date).format('dddd MMMM Do, YYYY');
                        response.data.assignments[i].due_date = moment(response.data.assignments[i].due_date).format('dddd MMMM Do, YYYY [at] h:mm:ss a');
                    }

                    this.unit = response.data;

                });
        }
    }
</script>

<style>
    .el-button {
        width: 100%;
        marigin-left: 0;
        border: 0;
        background-color: #fafafa;
    }

    .el-divider--vertical {
        height: 150px;
    }

    .small-font {
        font-size: 13px;
        color: #999;
    }

</style>