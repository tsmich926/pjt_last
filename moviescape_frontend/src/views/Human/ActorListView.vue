<template>
    <div>
        <div>
            <p>ActorListView</p>
            <HumanListItems :ITEMactors="actor_list"/>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import HumanListItems from '@/components/HumanListItems.vue'

export default {
name:'ActorListView',
components: {HumanListItems},

data() {
    return {

    actors: [],
    };
},
computed:{
    actor_list (){
        return this.actors
    }
},
methods: {
    getWholeActors(){
        axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/actors/`,
    })
    .then((res)=>{
        console.log(res.data)
        this.actors = res.data

    })
    .catch((err)=>{
        console.log(err)
            })
        }
    },
    created(){
    this.getWholeActors()
    }
};

</script>

<style>

</style>