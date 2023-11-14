<script setup>
import { postBike } from '../../requests/bikeRequests.js'
import { ref } from 'vue';
const formData = ref({})

const addBike = () => {
        console.log("Data...:", formData.value)
        postBike(formData.value)
    }
</script>

<template>
    <div class="location-form-container">
        <form v-on:submit.prevent="addBike">
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
            /><br>
            <span>Any notable features (broken parts, etc)</span><br>
            <input
                v-model="formData.notes"
                type="text"
                placeholder="Buckled wheel"
            /><br>
            <span>Location found at (id)</span><br>
            <input
                v-model="formData.location_id"
                type="text"
                placeholder="1"
            /><br>

            <button @click = "addBike()">Add a new bike!</button>
        </form>
    </div>
</template>
