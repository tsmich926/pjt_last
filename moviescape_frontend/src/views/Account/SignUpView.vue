<template>
  <div class="usersignupbox">
    <h1>SignUpView</h1>

      <form class="w-full" @submit.prevent="login">
        <SignInput
          :type="emailComponent"
          :value="email"
          @set-sign-value="setSignValue"
        />
      </form>
      
      <form v-on:submit.prevent="SignUp">
        <h2>Create an account</h2>
        <input type="text"  placeholder="UserName" v-model="username">
        <hr>
        <input type="password"  placeholder="Password" v-model="password1">
        <hr>
        <input type="password" placeholder="PasswordConfirm" v-model="password2">
        <input type="submit" value="Sign up">
        <p>Already have an account?
          <router-link to="/Login">Login</router-link>
        </p>
      </form>
    </div>
</template>

<script>
export default {
  name:'SignUpView',
  data(){
    return {
      username:null,
      password1:null,
      password2:null
    }
  },
  methods: {
    SignUp(){
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username,password1,password2
      }
      this.$store.dispatch('SignUp',payload)
    }
  }
}
</script>

<style>

</style>