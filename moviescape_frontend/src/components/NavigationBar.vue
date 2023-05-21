<template>
  <div>
     <nav class="navbar fixed-nav my_navBar"> <!--//여기에수정 -->
      <div class="scroll-wrapper">
        <a class="navbar-brand" href="/">
          <img src="@/assets/escape.webp" alt="Logo" width="30" height="24" class="d-inline-block align-text-top">
          Moviescape
        </a>
        <router-link :to="{name:'MovieListView'}">MovieListView</router-link>
        <router-link to="/MovieDetailView">MovieDetail</router-link>
        <router-link to="/RecommendView">Recommendation</router-link>
        <router-link to="/ReviewListView">ReviewListView</router-link>
        <router-link to="/ActorListView">ActorListView</router-link>
        <router-link v-show="!isLogin" to="/LoginView">로그인</router-link>
        <button v-show="isLogin" @click="LogOut" class="btn btn-primary">로그아웃</button>
        <img src="http://decoder.kr/wp-content/uploads/2020/03/decoder_smallver.gif" alt="Decoder / 디코더" width="50" height="50" >
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "NavigationBar",
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    }
  },
  methods: {
    LogOut() {
      this.$store.dispatch('LogOut');
    }
  }
}
</script>

<style scoped>
/* overflow-x: auto; */
#navbar-container {
  width: 100%;
}

nav a {
  font-weight: bold;
  color: #ffffff;
}

nav a.router-link-exact-active {
  color: #cee2c5;
}

.my_navBar {
  justify-content: center;
  align-content: center;
  text-align: center;
}

.scroll-wrapper {
  display: flex;
  justify-content: center;
  align-items: center; /*세로로 중앙 */
  padding: 10px;
  background-color: black;
  width: 100%;
}

.navbar-items {
  display: flex;
  align-items: center;
}

.scroll-wrapper > * {
  margin-right: 10px;
  white-space: nowrap; /* 줄바꿈 방지  */
}
</style>