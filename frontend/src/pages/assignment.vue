<template>
    <el-container>
        <el-aside>
            <!-- sidebar for list of assignments -->
            <assignmentsSideBar></assignmentsSideBar>
        </el-aside>
        <el-main>
            <!-- insert assignment component -->
            <codeAssignment v-if="assignment.type === 'code'" />
        </el-main>
    </el-container>
</template>

<script>
    import assignmentsSideBar from '../components/AssignmentsSideBar';

    import codeAssignment from './assignments/codeAssignment';

    export default {
        components: {
            assignmentsSideBar,
            codeAssignment
        },
        computed: {
            assignment() {
                if (this.$store.getters.courseLoaded){
                    return this.$store.getters.assignment(this.$route.params.id, this.$route.params.unit_id, this.$route.params.assignment_id);
                }
                else{
                    return {};
                }
            },
        },
    }
</script>

<style scoped>

</style>