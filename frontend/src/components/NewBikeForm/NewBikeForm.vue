<script setup>
import { postBike } from '../../requests/bikeRequests.js'
const bikeData = {
    "brand": "Shogun",
    "colour": "orange",
    "condition": "good",
    "date_found": "2023-09-13",
    "notes": "none",
    "location_id": 1
}

</script>

<template>
    <div class="location-form-container">
        <form>
            <v-select :options="locations" label="locations">Choose Location</v-select>
            <button @click = "postBike(bikeData)">Add a new bike!</button>
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