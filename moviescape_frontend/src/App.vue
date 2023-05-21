<template>
  <div id="app" class="super_space my_backgroundimg">
    <div class="nav_space"></div>
    <div class="my_content">
      <h1>여기는 App</h1>
      
      <NavigationBar />
    </div>
  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue'


export default {
  name:'app',

  components: {
    NavigationBar
  }
}
</script>

<style>
#app {
    background-color: rgb(71, 71, 71);
    color: white;
    width:100%;
    height:100%;
}
.my_backgroundimg{
  background-image: url('@/assets/Backgroundimg3.jfif');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  display: flex;
  justify-content: center; 
  height: 100%;
  /* pointer-events: none; */
  position: fixed;
  top: 0;
  width: 100%;
  /* align-items: center;*/
  /* border: none; */
  /* background-position: center bottom; */
}
.my_content{
  max-width: 80%; /* 내용의 최대 너비를 지정 */
  text-align: center; /* 내용을 가운데 정렬 */

}
.white-bg-box{
  background-color: white;

}
.nav_space{
  height:56px;
}
.super_space{
  overflow-x: auto;
}
</style>
