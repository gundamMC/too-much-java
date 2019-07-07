<template>

    <el-container>
        <el-aside>
            <sideBar :course_id="$route.params.id"/>
        </el-aside>
        <el-main>

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
                                <el-col :span="11" style="margin-top: 25px;">
                                    <el-button style="width: 100%; margin-left: 0">
                                        <el-row type="flex" align="middle" justify="center">
                                            Assignments
                                            <el-progress type="circle" :percentage="25" :width="50" status="text"
                                                         style="margin-left: 15%"></el-progress>
                                        </el-row>
                                    </el-button>

                                    <el-button style="width: 100%; margin-left: 0">
                                        <el-row type="flex" align="middle" justify="center">
                                            Assignments
                                            <el-progress type="circle" :percentage="25" :width="50" status="text"
                                                         style="margin-left: 15%"></el-progress>
                                        </el-row>
                                    </el-button>

                                    <el-button style="width: 100%; margin-left: 0">
                                        <el-row type="flex" align="middle" justify="center">
                                            Assignments
                                            <el-progress type="circle" :percentage="25" :width="50" status="text"
                                                         style="margin-left: 15%"></el-progress>
                                        </el-row>
                                    </el-button>

                                </el-col>
                                <el-col :span="2">
                                    <el-divider direction="vertical"></el-divider>
                                </el-col>
                                <el-col :span="11">
                                    <div style="text-align: left; margin-bottom: 10px;">
                                        <h3>Latest Assignments</h3>
                                    </div>
                                    <el-table :data="unit.latest" :row-style=bg_style :header-cell-style=bg_style>
                                        <el-table-column prop="name" label="Name"/>
                                        <el-table-column prop="type" label="Type"/>
                                        <el-table-column prop="due_date" label="Due"/>
                                    </el-table>
                                </el-col>
                            </el-row>
                        </div>
                    </collapseCard>

                </el-row>
            </div>
        </el-main>
    </el-container>


</template>

<script>
    import collapseCard from '../components/collapseCard.vue';
    import sideBar from '../components/SideBar';

    export default {
        components: {
            collapseCard,
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
            course() {
                if (this.$store.getters.courseLoaded){
                    return this.$store.getters.course(this.$route.params.id);
                }
                else{
                    return {};
                }
            }
        },
        created() {

            // for (let i = 0; i < this.course.units.length; i++) {
            //     this.$api.get(`/api/unit/${this.course.units[i].id}/latest/`)
            //         .then(unit_response => {
            //             this.$set(this.course.units[i], 'latest', unit_response.data.assignments);
            //         })
            // }

        }
    }
</script>

<style scoped>
    .el-button {
        width: 100%;
        marigin-left: 0;
        border: 0;
        background-color: #fafafa;
    }

    .el-divider--vertical {
        height: 150px;
    }

</style>