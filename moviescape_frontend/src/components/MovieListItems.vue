<template>
  <div>
    <h1>MovieListItems</h1>
    <div class="container text-center">
      <div class="row">
        <div class="col" v-for="movie in ITEMmovies" :key="movie.pk" >
          <MovieCard :CARDmovie="movie"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
// import MovieCard from '@/components/test2.vue'
export default {
  name:'MovieListItems',
  components:{
    MovieCard
  },
  data(){
    return{

    }
  },
  props:{
    ITEMmovies:Array
  },
  methods:{
    

  }

}
</script>

<style>
/* .my-min-card{
  display:flex;
  justify-content: center;
  flex-grow: 0;
  min-width: 200px;
  min-height: 400px;
} */
</style>