<template>
    <div>
        <el-card style="width: 340px; margin: 50px auto; padding: 10px">
            <h1 style="text-align: center">Login</h1>
            <el-form :rules="rules" :model="model">
                <el-form-item prop="username">
                    <el-input
                        v-model="model.username"
                        placeholder="Username"
                        prefix-icon="el-icon-user-solid">
                    </el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input
                        v-model="model.password"
                        placeholder="Password"
                        show-password
                        prefix-icon="el-icon-lock">
                    </el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" :loading="loading" @click="onSubmit" style="width: 100%">
                        Login
                    </el-button>
                </el-form-item>
            </el-form>

            <div>
                <el-popover
                content="Please contact your instructor to reset your password."
                placement="top-start"
                title="Reset password"
                trigger="hover"
                width="200"
                style="float: left">
                <el-button slot="reference" type="text">Forgot password</el-button>
              </el-popover>
              <el-button type="text" style="float: right;">Register</el-button>
            </div>
            
        </el-card>
    </div>
</template>

<script>

    export default {
        data () {
            return {
                model: {
                    username: '',
                    password: '',
                },
                rules: {
                    username: [
                      { required: true, message: "Username is required", trigger: "blur" }
                    ],
                    password: [
                      { required: true, message: "Password is required", trigger: "blur" }
                    ]
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
                this.$store.dispatch('obtainToken',
                    {username: this.model.username,password: this.model.password, responseMessage: (message) => {
                    this.$message({message: message, type: 'error'});
                }});
            }
        }
    }
</script>

<style scoped>

</style>