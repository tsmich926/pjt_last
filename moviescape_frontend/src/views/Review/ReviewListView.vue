<template>
  <div>
    <p>ReviewListView</p>
    <div v-for="review in review_list" :key="review.title" class="review-item">
      <h3>리뷰제목 : {{review.title}}</h3>
      <br>
      <h3>리뷰내용 : {{review.content}}</h3>
      <hr>
      <img :src="`https://image.tmdb.org/t/p/w500/${review.movie.poster_path}`" alt="">
      {{review.likes}}
      <br>
      {{review.movie.title}}
      <br>
      {{review.movie.overview}}
      <hr>
    </div>

    <div  class="article-section" > 
      <p>게시글</p>
      <input type="button" value="게시글 작성" @click="gotoCreateArticle" class="btn-create-article" >
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
export default {
  name:'ReviewListView',
  
  components: { 
    
  },
  data(){
    return{
      reviews:null,
    }
  },
  computed:{
    review_list(){
      return this.$store.state.reviews
    }
  },
  methods:{
    gotoCreateArticle(){
      this.$router.push({name:'CreateReviewView'})
    },
    // getReviews(){
    //   const API ='http://127.0.0.1:8000'
    //   axios({
    //     method:'get',
    //     url:`${API}/api/v1/reviews/`,
    //   })
    //   .then(res=>{
    //     console.log(res)
    //     this.reviews=res.data
    //   })
    //   .catch(err=>{
    //     console.log(err)
    //   })
    // }
  },
  created(){
    this.getReviews()
  }
}
</script>



<style scoped>
.btn-save,
.btn-list {
  width: 200px; /* 원하는 너비 값으로 수정 */
  height: 100px; /* 원하는 높이 값으로 수정 */
}

.review-item {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  margin-bottom: 20px;
}

.article-section {
  margin-top: 30px;
}

.btn-create-article {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  color: #fff;
  background-color: #008080;
  cursor: pointer;
  font-size: 14px;
}
</style>