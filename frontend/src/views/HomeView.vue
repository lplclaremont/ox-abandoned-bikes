<script setup>
    import { ref, onMounted } from 'vue';
    import { fetchBikes } from '../requests/bikeRequests.js';
    import Bike from '../components/Bike/Bike.vue'
    import NewBikeForm from '../components/NewBikeForm/NewBikeForm.vue'

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
        <NewBikeForm />
        <div v-for="bike in bikes" class="bikes-container">
            <Bike v-bind="bike" />
        </div>
    </main>
</template>

<style scoped>
h1 {
    color: rgb(236, 36, 172);
    font-size: 350%;
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
}

main {
    min-width: 200vh;
    min-height: 100vh;
    margin: 0;
    padding-left: 40px;
}
</style>