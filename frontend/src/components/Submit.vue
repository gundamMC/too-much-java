<template>
    <div>
        <el-upload class="upload"
                   ref="upload"
                   drag
                   action="/api/upload/"
                   :data="{submission: sub_id}"
                   :multiple="true"
                   :headers="{ 'X-CSRFToken': csrf}"
                   :auto-upload="false"
                    style="width: 360px"
        >
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">Drop file here or <em>click to upload</em></div>
            <div slot="tip" class="el-upload__tip">.java files with a size less than 1.0 mb</div>
        </el-upload>

        <el-row style="margin-top: 20px">
            <el-button type="primary" @click="submitUpload">Confirm upload</el-button>

            <el-button type="info" @click="clearFiles">Clear files</el-button>
        </el-row>




    </div>
</template>

<script>

    import axios from 'axios';

    export default {
        props: {
            assignment: Object,
            student_id: Number
        },
        data() {
            return {
                csrf: this.$cookies.get('csrftoken'),
                submission: {},
                sub_id: null
            }
        },
        methods: {
            submitUpload() {

                // create submission first
                axios
                    .post(`/api/submission/`, {'assignment': this.assignment.id, 'student': this.student_id})
                    .then(response => {

                        this.submission = response.data;

                        this.sub_id = response.data.id;

                        console.log(response.data);

                        this.$nextTick(
                            () => (this.$refs.upload.submit())
                        );

                    });


            },

            clearFiles() {
                this.$refs.upload.clearFiles();
            }
        }
    }
</script>

<style scoped>

</style>