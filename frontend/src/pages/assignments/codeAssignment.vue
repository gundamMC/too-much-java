<template>

    <el-card>
        <el-row>
            <h1>Practice Programming Assignment: Python Basics with numpy (optional)</h1>
        </el-row>
        <el-row>
            <i class="el-icon-circle-check"></i> Passed · 100/100 points
        </el-row>

        <el-row>
            <b>Deadline</b>
            <span style="margin-left: 10px">The assignment was due on December 31, 11:59 PM PST</span>
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
                        Download the project related files here.
                    </el-row>

                    <el-row type="flex">
                        <i class="el-icon-files" style="font-size: 60px"></i>
                        <div style="margin-left: 20px">
                            <h2>test_file.zip</h2>
                            10.2 mb
                        </div>

                        <el-button type="primary" style="margin-left: 100px; width: 250px">Download</el-button>

                    </el-row>

                    <el-divider></el-divider>

                    <el-row>
                        <small>
                            Due to current limitations, only one file is allowed per assignment.
                            For assignments with multiple files, please zip them into a single file.
                        </small>
                    </el-row>
                </el-tab-pane>

                <el-tab-pane label="My Submissions">My Submissions</el-tab-pane>
            </el-tabs>
        </el-row>

    </el-card>

</template>

<script>
    export default {
        name: "assignment"
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