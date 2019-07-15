<template>

    <el-container>
        <el-aside>
            <sideBar :course_id="$route.params.unit_id"/>
        </el-aside>
        <el-main>

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
                            <el-timeline-item :key="assignment.id" :timestamp="assignment.date" placement="top"
                                              v-for="assignment in unit.assignments">
                                <router-link :to="'assignment/' + assignment.id + '/'">
                                    <el-card shadow="hover">
                                        <div slot="header">
                                            <i class="el-icon-document" v-if="assignment.type === 'code'"></i>
                                            <i class="el-icon-menu" v-else-if="assignment.type === 'quiz'"></i>
                                            <i class="el-icon-notebook-2" v-else></i>
                                            <span>    {{assignment.name}}</span>
                                        </div>
                                        <p>{{assignment.description}}</p>
                                        <p class="small-font">Due: {{assignment.due_date}}</p>
                                    </el-card>
                                </router-link>
                            </el-timeline-item>
                        </el-timeline>
                    </div>

                </el-row>
            </div>
        </el-main>
    </el-container>

</template>

<script>
    import sideBar from '../components/SideBar';

    export default {
        components: {
            sideBar
        },
        data() {
            return {
                bg_style: {
                    backgroundColor: "#fafafa"
                }
            }
        },
        computed: {
            unit() {
                if (this.$store.getters.courseLoaded){
                    return this.$store.getters.unit(this.$route.params.id, this.$route.params.unit_id);
                }
                else{
                    return {};
                }
            }
        }

    }
</script>

<style scoped>
    .small-font {
        font-size: 13px;
        color: #999;
    }

</style>