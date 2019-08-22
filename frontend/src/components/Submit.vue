<template>
    <div>
        <el-upload class="upload"
                   ref="upload"
                   drag
                   action="/api/upload/"
                   :data="{submission: sub_id}"
                   :multiple="true"
                   :headers="{ 'X-CSRFToken': csrf, 'Authorization': 'jwt ' + this.$store.getters.token}"
                   :auto-upload="false"
                   :on-success="onSuccess"
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
                this.$api
                    .post(`submission/`, {'assignment': this.assignment.id})
                    .then(response => {

                        this.submission = response.data;

                        this.sub_id = response.data.id;

                        this.$nextTick(
                            () => (this.$refs.upload.submit())
                        );
                    });


            },

            clearFiles() {
                this.$refs.upload.clearFiles();
            },

            onSuccess() {

                // clear files to prevent student from clicking twice
                this.$refs.upload.clearFiles();

                this.$api
                    .get('submission/' + this.sub_id + '/grade/')
                    .then(response => (this.$store.dispatch('setSubmissions', response.data)));

                // setTimeout(() => this.$store.dispatch('getSubmissions', this.assignment.id), 10000);
                        // refresh submissions after 10 seconds

            }
        }
    }
</script>

<style scoped>

</style>