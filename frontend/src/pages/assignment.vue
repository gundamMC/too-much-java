<template>
    <el-container>
        <el-aside>
            <!-- sidebar for list of assignments -->
            <assignmentsSideBar></assignmentsSideBar>
        </el-aside>
        <el-main>
            <!-- insert assignment component -->
            <codeAssignment/>
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
        }
    }
</script>

<style scoped>

</style>