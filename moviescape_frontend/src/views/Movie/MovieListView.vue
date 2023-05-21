<template>
  <div class= "my_MovieListView_BGC">
    <h1>MovieListView</h1>
    <div>
      <MovieListItems :ITEMmovies="movie_list"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListItems from '@/components/MovieListItems.vue'
export default {
  name:'MovieListView',
  components:{
    MovieListItems
  },
  data(){
    return {
      movies:[]
    }
  },
  computed:{
    movie_list(){
      return this.movies
    }
  },
  methods:{
    getWholeMovies(){
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/api/v1/movies/'
      })
      .then(res=>{
        console.log(res)
        this.movies=res.data
      })
      .catch(err=>{
        console.log(err)
      })
    }
  },
  created(){
    this.getWholeMovies()
  }
}
</script>

<style scoped>
.my_MovieListView_BGC{
  background-color: #575656;
}
</style>