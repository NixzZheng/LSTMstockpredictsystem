<template>
   <div class="login-container">
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form" auto-complete="on" label-position="left">
        <div class="title-container">
            <h3 class="title">登录</h3>
        </div>

        <el-form-item prop="username">
            <span class="svg-container">
                <svg-icon icon-class="user" />
            </span>
            <el-input
          ref="username"
          v-model="loginForm.username"
          placeholder="Username"
          name="username"
          type="text"
          tabindex="1"
          auto-complete="on"
        />
        </el-form-item>
        <el-form-item prop="password">
            <span class="svg-container">
                <svg-icon icon-class="lock" />
            </span>
            <el-input
          ref="password"
          v-model="loginForm.password"
          placeholder="Password"
          name="password"
          type="password"
          tabindex="2"
          auto-complete="on"
          @keyup.enter.native="handleLogin"
        />
          <span class="show-pwd" @click="showPwd">
            <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
          </span>
        </el-form-item>

        <el-button :loading="loading" type="primary" style="width:100%;margin-bottom:30px;" @click.native.prevent="handleLogin">Login</el-button>
        <div class="tips">
            <span style="margin-right:20px;font-size: 1ch;">username: admin</span>
            <span style="margin-right:20px;font-size: 1ch;">password: 123456</span>
            
        </div>
    </el-form>
   </div>
</template>

<script>
import { validUsername } from '@/utils/validate'

export default {
  name: 'Login',
  data(){
    const validateUsername = (rule, value, callback) => {
      if (!validUsername(value)) {
        callback(new Error('Please enter the correct user name'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('The password can not be less than 6 digits'))
      } else {
        callback()
      }
    }
    return {
      loginForm: {
        username: 'admin',
        password: '123456'
      },
      loginRules: {
        username: [{ required: true, validator: validateUsername, trigger: 'blur' }],
        password: [{ required: true, validator: validatePassword, trigger: 'blur' }]
      },
      loading: false,
      passwordType: 'password',
      redirect: undefined
    }
  },
    methods: {
        showPwd() {
        if (this.passwordType === 'password') {
          this.passwordType = 'text'
        } else {
          this.passwordType = 'password'
        }
        this.$nextTick(() => {
          this.$refs.password.focus()
        })
    },
    handleLogin() {
      this.$refs.loginForm.validate((valid) => {
        if (valid) {
          this.loading = true
          this.$store
            .dispatch('user/login', this.loginForm)
            .then(() => {
              this.loading = false
              this.$router.push({ path: this.redirect || '/' })
            })
            .catch(() => {
              this.loading = false
            })
        } else {
          return false
        }
      })
    }
  }
}
</script>

<style scoped>

.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

</style>