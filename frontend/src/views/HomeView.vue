<script setup>
  import { ref, onMounted } from 'vue';
  import { fetchBikes } from '../requests/bikeRequests.js';
  import Bike from '../components/Bike.vue'

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
    <li v-for="bike in bikes">
      {{ bike }}
      <div>
        <Bike v-bind="bike" />
      </div>
    </li>
    
  </main>
</template>

<style scoped>
</style>