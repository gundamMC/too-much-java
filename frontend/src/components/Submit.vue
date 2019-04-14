<template>
    <div>
        <h1>Submit your .java file below for submission {{submission.id}} : </h1>

        <el-button style="margin: 10px;" size="small" type="success" @click="submitUpload">Confirm upload</el-button>

        <el-upload class="upload"
                   ref="upload"
                   drag
                   action="/api/upload/"
                   :data="{submission: submission.id}"
                   :multiple="true"
                   :headers="{ 'X-CSRFToken': csrf}"
                   :auto-upload="false"
                   :on-remove="(file, f_list) => {t_file=file; fileList=f_list;}">
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">Drop file here or <em>click to upload</em></div>
            <div slot="tip" class="el-upload__tip">.java files with a size less than 1.0 mb</div>
        </el-upload>

        {{t_file}}  <!-- if status == success -> file is already sent, ready -> not sent yet

        { "status": "success", "name": "AP_Chemistry.pdf", "size": 113494, "percentage": 100, "uid": 1554083008629, "raw": { "uid": 1554083008629 }, "response": { "id": 3, "file": "http://localhost:8000/api/upload/uploads/2019/03/31/AP_Chemistry_atCkHoH.pdf", "submission": 4 } }

        -->

        ------------------

        {{fileList}}

    </div>
</template>

<script>
    export default {
        props: {
            submission: Object
        },
        data() {
            return {
                csrf: this.$cookies.get('csrftoken'),
                t_file: null,
                fileList: null
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