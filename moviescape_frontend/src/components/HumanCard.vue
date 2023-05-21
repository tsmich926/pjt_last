```
<template>
    <div class="row">
        <div class="col-md-3">
            <div class="card" style="width: 18rem;" @mouseenter="zoomInCard" @mouseleave="zoomOutCard">
                <img :src="`https://image.tmdb.org/t/p/w500/${CARDactor.profile_path}`" class="card-img-top" alt="Actor Image">
                <div class="card-body">
                <h5 class="card-name">{{CARDactor.name }}</h5>
                <button 
              type="button" 
              @click="likeActor()"
              class="btn btn-outline-primary"
            >
            {{ liked ? '❤': '🤍'}}
            </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
name:'HumanCard',
data() {
  return {
    liked: false
  }
},
methods: {
    
    // toggleLike(actor) {
    //좋아요 로직---
    // },
    zoomInCard(event) {
      // 카드 확대하는 로직 구현
    event.target.classList.add('zoom-in');
    },
    zoomOutCard(event) {
      // 카드 축소하는 로직 구현
    event.target.classList.remove('zoom-in');

  },

    likeActor() {
      // 좋아요 로직 구현
      this.liked = !this.liked;
    }

},
props:{
CARDactor:Object
    },

}


</script>



<style scoped>
.row {
  display: flex;
  flex-wrap: wrap;
  margin: -15px;
}

.col-md-3 {
  width: 25%;
  padding: 15px;
  box-sizing: border-box;
}
</style>