<template>
  <div>
    <p>MovieSearchItems</p>
    <h1>검색할 제목을 입력</h1>
    <input type="text" v-model="title" @input="getMovie">
    <button @click="toNull">초기화</button>
    <div>
      <div v-for="movie in movies" :key="movie.pk">
       <div>
          <h3>
            <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="">
          </h3>
          <h3>{{movie.title}}</h3>
          <h3>{{movie.overview}}</h3>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
export default {
  name:'MovieSearchItems',
  data(){
    return{
      title:null,
      movie_list:null,
    }
  },
  methods:{
    getMovie(){
      const title=this.title
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/movies/search/${title}/`

      })
      .then(res=> {
        console.log(res)
        this.movie_list=res.data
      })
      .catch(err=>{
        console.log(err)
      })
    },
    toNull(){
      this.title=null
    }
  },
  computed:{
    movies(){
      return this.movie_list
    }
  }

}
</script>

<style>

</style>