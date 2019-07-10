<template>
    <div>
        <el-card style="width: 340px; margin: 50px auto; padding: 10px">
            <h1 style="text-align: center">Register</h1>

            <el-divider></el-divider>

            <el-form :rules="rules" :model="model" ref="form">
                <el-form-item prop="username">
                    <el-input
                        v-model="model.username"
                        placeholder="Username"
                        prefix-icon="el-icon-user-solid">
                    </el-input>
                </el-form-item>
                <el-form-item prop="student_id">
                    <el-input
                        v-model.number="model.student_id"
                        placeholder="Student ID"
                        prefix-icon="el-icon-collection-tag">
                    </el-input>
                </el-form-item>
                <el-form-item prop="grade">
                    <el-select v-model="model.grade"
                               placeholder="Grade">
                          <el-option label="Freshman" :value="9"></el-option>
                          <el-option label="Sophomore" :value="10"></el-option>
                          <el-option label="Junior" :value="11"></el-option>
                          <el-option label="Senior" :value="12"></el-option>
                    </el-select>
              </el-form-item>
                <el-form-item prop="password">
                    <el-input
                        v-model="model.password"
                        placeholder="Password"
                        show-password
                        prefix-icon="el-icon-lock">
                    </el-input>
                </el-form-item>
                <el-form-item prop="confirmPassword">
                    <el-input
                            v-model="model.confirmPassword"
                        placeholder="Confirm Password"
                        show-password
                        prefix-icon="el-icon-lock">
                    </el-input>
                </el-form-item>

                <el-divider></el-divider>

                <el-form-item prop="code">
                    <el-input
                        v-model="model.code"
                        placeholder="Course Code"
                        prefix-icon="el-icon-connection">
                    </el-input>
                </el-form-item>

                <el-form-item>
                    <el-button type="primary" :loading="loading" @click="onSubmit" style="width: 100%">
                        Register
                    </el-button>
                </el-form-item>
            </el-form>

            <div>
              <el-button type="text" style="float: right;">Login</el-button>
            </div>
            
        </el-card>
    </div>
</template>

<script>

    export default {
        data () {

            var validatePassMatch = (rule, value, callback) => {
                if (value !== this.model.password) {
                  callback(new Error('The passwords do not match!'));
                } else {
                  callback();
                }
              };

            return {
                model: {
                    username: '',
                    password: '',
                    student_id: '',
                    grade: null,
                    code: ''  // using underscore b/c that's what python uses
                },
                rules: {
                    username: [
                      { required: true, message: "Username is required", trigger: "blur" }
                    ],
                    password: [
                      { required: true, message: "Password is required", trigger: "blur" }
                    ],
                    confirmPassword: [
                      { required: true, message: "Enter your password again", trigger: "blur" },
                        { validator: validatePassMatch, trigger: "blur"}
                    ],
                    student_id: [
                        { required: true, message: 'Student ID is required'},
                        { type: 'number', message: 'Student ID must be a number'}
                    ],
                    grade: [
                      { required: true, message: "Grade is required", trigger: "blur" }
                    ],
                    code: [
                      { required: true, message: "Course Code is required", trigger: "blur" }
                    ],
                  }
            }
        },
        computed: {
            loading () {
                return this.$store.getters.loginLoading;
            }
        },
        methods: {
            onSubmit () {
                this.$refs.form.validate((valid) => {
                    if (valid){
                        this.$api
                    .post('register/', this.model)
                    .then(() => {
                        // success, now grab a token
                        this.$store.dispatch('obtainToken',
                            {username: this.model.username, password: this.model.password, responseMessage: (message) => {
                            this.$message({message: message, type: 'error'});
                        }});
                      })
                      .catch(error => {
                          if (error.response.status === 400){
                              for (let i = 0; i < error.response.data.length; i++){
                                this.$message({message: error.response.data[i], type: 'error'});
                            }
                          }
                          else if (error.response.status === 500){
                              if (error.response.data.includes('UNIQUE constraint failed: auth_user.username')){
                                  this.$message({message: 'Username already used', type: 'error'});
                              }
                          }
                      });
                    } else {
                        this.$message({message: "Invalid registration information!", type: 'error'});
                    }
                });


            }
        }
    }
</script>

<style scoped>

</style>