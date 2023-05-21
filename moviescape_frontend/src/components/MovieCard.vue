<template>
    <div class="bg-secondary card my-card" >
      <img :src="`https://image.tmdb.org/t/p/w500/${CARDmovie.poster_path}`" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title my-card-title">{{CARDmovie.title}}</h5>
        <p class="card-text my-card-text">{{CARDmovie.overview}}</p>
      </div>
    </div>
</template>

<script>
export default {
  name:'MovieCard',
  props:{
    CARDmovie:Object
  },
  components:{

  },
  methods:{

  }

}
</script>

<style scoped>
.my-card-text {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
  text-overflow: ellipsis;
  word-wrap: break-word;
}
.my-card-title {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
  text-overflow: ellipsis;
  word-wrap: break-word;
}
.my-card {
  width: 18rem;
  height: 38rem;
  margin-bottom: 30px;
  padding: 0px;
  flex-shrink: 0;
}
</style>