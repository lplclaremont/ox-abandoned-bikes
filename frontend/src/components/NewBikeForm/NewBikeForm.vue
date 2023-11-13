<script setup>
import { postBike } from '../../requests/bikeRequests.js'
</script>

<template>
    <div class="location-form-container">
        <form>
            <button @click = "console.log('New bike added!')">Add a new bike!</button>
        </form>
    </div>
</template>

<script>
export default {
    data () {
        return {
            locations: [
                {location: "Mag bridge"},
                {location: "Westgate"}
            ]
        };
    }
};
</script>