<script setup>
  import { ref, onMounted } from 'vue';
  import { fetchBikes } from '../requests/bikeRequests.js';

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
    <h1>Home page here!</h1>
    <li v-for="bike in bikes">
      {{ bike }}
    </li>
    
  </main>
</template>

<style scoped>
</style>