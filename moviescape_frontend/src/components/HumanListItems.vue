<template>
  <div>
    <h1>HumanListItems</h1>
      <div v-for="actor in ITEMactors" :key="actor.pk" >
        <HumanCard :CARDactor="actor"/>
      </div> 
  </div>
</template>

<script>
import HumanCard from '@/components/HumanCard.vue'

export default {
  name:'HumanListItems',
  components:{
    HumanCard
  },

  props:{
    ITEMactors:Array
  },
  methods:{

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

    }

}
</script>

<style>
.card{
  background-color: rgb(157, 178, 191);
  transition: transform 0.3s ease;
}


.card.zoom-in {
  transform: scale(1.1);
}

.card-title {
  color: black;
}
</style>