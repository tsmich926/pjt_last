<template>
  <div class="login-view">
    <h1>LoginView</h1>
    <div class="userloginbox">
      <form v-on:submit.prevent="LogIn">
        <div class="form-group">
          <input type="text"  class="form-control" placeholder="userName" v-model="username" required>
        </div>
        <div class="form-group">
          <input type="password"  class="form-control" placeholder="userPassWord" v-model="password" required>
        </div>
        <br>
        <input type="submit" class="btn btn-primary" value="Login">
        <p class="signup-text">don't have an account?
          <router-link to="/SignUpView">signup</router-link>
          <!-- <a href="javascript:void(0);" @click="toggleForm">Sign up</a> -->
        </p>
      </form>
    </div>
  </div>
</template>


<script>
export default {
  name: 'LoginView' ,
  data(){
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    LogIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username,password
      }

      this.$store.dispatch('LogIn',payload)
    },
    // logout()
  }
}


</script>

<style scoped>

/* .userloginbox {
  width: 800px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
} */

.login-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 50vh;
}

.userloginbox {
  width: 400px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.form-group {
  margin-bottom: 20px;
}


.form-control {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid hsl(0, 30%, 92%);
  border-radius: 4px;
}

.btn-primary {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: none;
  border-radius: 4px;
  background-color: #063308;
  color: #fff;
  cursor: pointer;
}

.signup-text {
  text-align: center;
  margin-top: 10px;
  font-size: 14px;
}

.signup-text a {
  color: #e50914;
  text-decoration: none;
  font-weight: bold;
}

</style>

