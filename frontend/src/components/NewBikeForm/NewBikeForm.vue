<script setup>
import { postBike } from '../../requests/bikeRequests.js'
import { fetchLocations } from '../../requests/locationRequests.js'
import { ref, onMounted } from 'vue';
const formData = ref({notes: null});
const locations = ref([]);

const loadLocations = async () => {
    try {
        const data = await fetchLocations();
        locations.value = data
    } catch (error) {
        console.log(error);
    }
}
    
onMounted(() => {
    loadLocations();
})

const addBike = () => {
        console.log("Data...:", formData.value)
        postBike(formData.value)
    }

</script>

<template>
    <div class="location-form-container">
        <h2>Log a new bike here:</h2>
        <form>
            <span>Brand name</span><br>
            <input 
                v-model="formData.brand"
                type="text"
                placeholder="Dawes"
                required
            /><br>
            <span>Colour</span><br>
            <input 
                v-model="formData.colour"
                type="text"
                placeholder="Red"
                required
            /><br>
            <span>Condition</span><br>
            <select v-model="formData.condition" required>
                <option value="" disabled selected>Choose a condition</option>
                <option value="poor">Poor</option>
                <option value="fair">Fair</option>
                <option value="good">Good</option>
                <option value="excellent">Excellent</option>
            </select><br>
            <span>Date found</span><br>
            <input
                v-model="formData.date_found"
                type="text"
                placeholder="yyyy-mm-dd"
                required
            /><br>
            <span>Any notable features (broken parts, etc)</span><br>
            <input
                v-model="formData.notes"
                type="text"
                placeholder="Buckled wheel"
            /><br>
            <span>Location found</span><br>
            <select v-model="formData.location_id">
                <option value="" disabled selected>Choose a location</option>
                <option v-for="location in locations" :value="location.id">
                    {{ location.name }}
                </option>
            </select><br>

            <button @click = "addBike()">Add a new bike!</button>
        </form>
    </div>
</template>
