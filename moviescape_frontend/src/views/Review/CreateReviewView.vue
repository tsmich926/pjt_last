<template>
  <div>
    <h1>CreateReviewView</h1>
    <h2>새로운 글 등록</h2>
    <div class="board-detail">
      <form action="">
        <div class="board-contents">
          <div class="search-wrapper">
            <input type="text" v-model.trim="searchQuery" class="search-input" placeholder="영화를 검색하세요">
            <input type="button" @click="searchMovie" class="search-button">
              <i class="search-result">영화를 선택하셨습니다</i>

          </div>
          <label for="title">제목</label>
          <input type="text" v-model.trim="title" class=" input-field " placeholder="제목을 입력해주세요."><br>
          <label for="input">내용</label>
          <textarea id="content" cols="30" rows="10" v-model="content" placeholder="리뷰를 작성해주세요."></textarea><br>
        </div>
      </form>
      <div class="common-buttons">
        <input type="button" @click="saveArticle" class="btn btn-primary" style="background-color: #008080;" value="작성완료">&nbsp;
        <input type="button" @click="gotoComunityView" class="btn btn-primary" style="background-color: #008080;" value="목록">&nbsp;

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default { 
  name:'CreateReviewView',
  data(){
    return{
      content:null,
      title:null,
    }
  },
  methods:{
    gotoComunityView(){
      this.$router.push({name:'Community'})
    },
    saveArticle(){
      const API ='http://127.0.0.1:8000'
      
      const title = this.title
      const content = this.content

      if(!title){
        alert('제목을 입력하세요')
      } else if (!content){
        alert('내용을 입력하세요')
        return
      }
    
      axios({
        method:'post',
        url:`${API}/api/v1/movies/38015/review/`,
        data: {
          title,
          content,
          },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res)=>{
        console.log(res)
        this.$router.push({name:'ReviewListView'})
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  },
  computed:{
    

  },

}
</script>

<style>
.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
  font-size: 14px;
}

.input-field {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 10px;
}

textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 10px;
}


.search-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}


</style>