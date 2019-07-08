<template>

    <el-card style="padding: 20px; margin: 0 40px;">
        <el-row>
            <h1>{{assignment.name}}</h1>
        </el-row>
        <el-row>
            <i class="el-icon-circle-check"></i> Passed · {{assignment.highest_points}}/{{assignment.points}} points
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
                                    <h2>test_file.zip</h2>
                                    10.2 mb
                                </div>

                                <el-button type="primary" style="margin-left: 100px; width: 250px">Download</el-button>

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

                        <el-collapse>
                            <el-collapse-item title="Consistency" name="1">
                                <div>Consistent with real life: in line with the process and logic of real life, and comply with languages and habits that the users are used to;</div>
                                <div>Consistent within interface: all elements should be consistent, such as: design style, icons and texts, position of elements, etc.</div>
                            </el-collapse-item>

                        </el-collapse>
                    </el-row>

                </el-tab-pane>
            </el-tabs>
        </el-row>

    </el-card>

</template>

<script>
    import submit from '../../components/Submit';
    import markdown from '../../components/Markdown';

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
                if (this.$store.getters.courseLoaded){
                    return this.$store.getters.assignment(this.$route.params.id, this.$route.params.unit_id, this.$route.params.assignment_id);
                }
                else{
                    return {};
                }

            },
            load_markdown() {
                return this.$store.getters.courseLoaded && this.assignment.instructions != null;
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