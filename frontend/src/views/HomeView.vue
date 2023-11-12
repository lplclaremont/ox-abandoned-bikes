<script setup>
  import { ref, onMounted } from 'vue';
  import { fetchBikes } from '../requests/bikeRequests.js';
  import Bike from '../components/Bike/Bike.vue'

  const bikes = ref([])

  const loadBikes = async () => {
    try {
      const data = await fetchBikes();
      bikes.value = data
    } catch (error) {
      console.log(error);
    }
  }
  
  onMounted(() => {
    loadBikes();
  })
</script>

<template>
  <main>
    <h1>Oxford's Abandoned Bikes!</h1>
      <div v-for="bike in bikes" class="bikes-container">
        <Bike v-bind="bike" />
      </div>
    
  </main>
</template>

<style scoped>
</style>