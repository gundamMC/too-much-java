<template>

    <el-card style="padding: 20px; margin: 0 40px;">
        <el-row>
            <h1>{{assignment.name}}</h1>
        </el-row>
        <el-row>
            <i :class="statusIcon"></i> {{status}} · {{statusHighestPoint}}/{{assignment.points}} points
        </el-row>

        <el-row>
            <b>Deadline</b>
            <span style="margin-left: 10px">The assignment is due on {{assignment.due_date}}</span>
        </el-row>

        <el-row>
            <el-tabs>
                <el-tab-pane label="Instructions">
                    <el-row>
                        <el-col :span="18">
                            <p>
                               Click on "My submission" above to see your grades.
                            It might take up to one minute for our graders to process your submission.
                            You will see the point break down of your assignment along with the grader feedback.
                            </p>
                            <el-row>
                                <h2>Overview</h2>
                                <p>
                                    {{assignment.description}}
                                </p>
                            </el-row>
                            <el-divider></el-divider>
                            <el-row>
                                <markdown v-if="load_markdown" :source="assignment.instructions"></markdown>
                            </el-row>

                        </el-col>
                        <el-col :span="6">
                            <div class="instruction_sidebar">
                                <h1>How to submit</h1>
                                <p>
                                    When you're ready to submit, you can upload files for each part of the assignment
                                on the "My submission" tab.
                                </p>
                            </div>

                            <div class="instruction_sidebar">
                                <h1>Provided files</h1>
                                <p>
                                    The files of assignments are available for download in the "Files" tab.
                                </p>
                            </div>

                        </el-col>
                    </el-row>
                </el-tab-pane>

                <el-tab-pane label="Files">
                    <el-row>
                        <el-col :span="18">

                            <p>Download the project related files here.</p>

                            <el-row type="flex">
                                <i class="el-icon-files" style="font-size: 60px"></i>
                                <div style="margin-left: 20px">
                                    <h2>{{assignment.file_name}}</h2>
                                    {{assignment.file_size}}
                                </div>

                                <el-button type="primary" style="margin-left: 100px; width: 250px" @click="download">Download</el-button>

                            </el-row>

                        </el-col>
                        <el-col :span="6">
                            <div class="instruction_sidebar">
                                <h1>Multiple Files</h1>
                                <p>
                                Due to current limitations, only one file is allowed per assignment.
                            For assignments with multiple files, please zip them into a single file.
                                </p>
                            </div>
                        </el-col>
                    </el-row>
                </el-tab-pane>

                <el-tab-pane label="My Submissions">

                    <el-row>

                        <el-col :span="18">

                            <h1>Upload a new submission</h1>
                            <submit :assignment="assignment" :student_id="1"></submit>

                        </el-col>

                        <el-col :span="6">
                            <div class="instruction_sidebar">
                                <h1>Multiple Files</h1>
                                <p>
                                    To upload multiple files at once, simple drag them to the drop-off area
                                    at once or select all of them (either at once or one by one) in the
                                    file selection window.
                                </p>
                            </div>
                        </el-col>
                    </el-row>

                    <el-divider></el-divider>

                    <el-row>
                        <h2>Submissions</h2>

                        <el-collapse v-if="submissions.length > 0">
                            <el-collapse-item
                                    v-for="submission in submissions"
                                    :title="submission.submitted_date + ' - ' + submission.points + '/' + assignment.points"
                                    :name="submission.id"
                                    :key="submission.id">
                                <el-table
                                        v-if="submission.checks.length > 0"
                                        :data="submission.checks"
                                        style="width: 100%">
                                    <el-table-column
                                            prop="name"
                                            label="Test Name"
                                            width="180">
                                    </el-table-column>
                                    <el-table-column
                                            prop="details"
                                            label="Details">
                                    </el-table-column>
                                </el-table>
                                <p v-else>
                                    Unexpected error. (Typically a compilation error)
                                </p>
                            </el-collapse-item>

                        </el-collapse>
                        <p  v-else>
                           Upload a new submission to see your results.
                        </p>
                    </el-row>

                </el-tab-pane>
            </el-tabs>
        </el-row>

    </el-card>

</template>

<script>
    import submit from '../../components/Submit';
    import markdown from '../../components/Markdown';
    import settings from '../../settings';

    export default {
        components: {
            submit,
            markdown
        },
        data() {
            return {
            }
        },
        computed: {
            assignment() {
                return this.$store.getters.assignment(this.$route.params.id, this.$route.params.unit_id, this.$route.params.assignment_id);
            },
            load_markdown() {
                return this.$store.getters.courseLoaded && this.assignment.instructions != null;
            },
            submissions() {
                return this.$store.getters.submissions;
            },
            status() {
                switch (this.assignment.highest_points){
                    case -1:
                        return "Not attempted";
                    case this.assignment.points:
                        return "Passed";
                    default:
                        return "Attempted";
                }
            },
            statusIcon() {
                switch (this.assignment.highest_points){
                    case -1:
                        return "el-icon-warning-outline";
                    case this.assignment.points:
                        return "el-icon-circle-check";
                    default:
                        return "el-icon-circle-plus-outline";
                }
            },
            statusHighestPoint() {
                if (this.assignment.highest_points === -1)
                    return "-";
                else
                    return this.assignment.highest_points;
            }

        },
        created() {
            this.$store.dispatch('getSubmissions', this.$route.params.assignment_id);
        },
        methods: {
            download() {
                window.open(settings.download_domain + '/' + this.assignment.code_template);
            }
        }
    }
</script>

<style scoped>
    .el-row {
        margin-top: 30px
    }

    .instruction_sidebar {
        background-color: #fbfbfb;
        padding: 20px;
        margin-left: 10px;
        margin-bottom: 30px;
    }

</style>