<template>
    <div>
        <h1>Submit your .java file below: </h1>

        <el-button style="margin: 10px;" size="small" type="success" @click="submitUpload">Confirm upload</el-button>

        <el-upload class="upload"
                   ref="upload"
                   drag
                   action="/api/upload/"
                   :multiple="true"
                   :headers="{ 'X-CSRFToken': csrf}"
                   :auto-upload="false">
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">Drop file here or <em>click to upload</em></div>
            <div slot="tip" class="el-upload__tip">.java files with a size less than 1.0 mb</div>
        </el-upload>

    </div>
</template>

<script>
    export default {
        name: "submit",
        data() {
            return {
                csrf: this.$cookies.get('csrftoken')
            }
        },
        methods: {
            submitUpload() {
                this.$refs.upload.submit();
            }
        }
    }
</script>

<style scoped>

</style>