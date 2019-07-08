<template>
    <div>
        <el-menu router :default-openeds="['/course/' + course_id]" :default-active="$route.fullPath">
            <el-menu-item v-for="assignment in assignments" :key="assignment.id" :index="'/course/' + course_id + '/unit/' + unit_id + '/assignment/' + assignment.id + '/'">
                <span slot="title">{{assignment.name}}</span>
            </el-menu-item>
        </el-menu>
    </div>
</template>

<script>

    export default {
        data() {
            return {
                course_id: this.$route.params.id,
                unit_id: this.$route.params.unit_id
            }
        },
        computed: {
            assignments() {
                if (this.$store.getters.courseLoaded){
                    return this.$store.getters.unit(this.course_id, this.unit_id).assignments;
                }
                else{
                    return {};
                }
            }
        }
    }

</script>

<style scoped>

</style>