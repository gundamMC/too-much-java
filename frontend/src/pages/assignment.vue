<template>
    <el-container>
        <el-aside>
            <!-- sidebar for list of assignments -->
        </el-aside>
        <el-main>
            <!-- insert assignment component -->
            <codeAssignment/>
        </el-main>
    </el-container>
</template>

<script>

    import codeAssignment from './assignments/codeAssignment';

    export default {
        components: {
            codeAssignment
        }
    }
</script>

<style scoped>

</style>