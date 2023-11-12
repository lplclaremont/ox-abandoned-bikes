<script setup>
import BikeIcon from '../BikeIcon/BikeIcon.vue';
import gears from '../../assets/gears.svg';
import dateIcon from '../../assets/dateIcon.svg';
defineProps(['id', 'brand', 'colour', 'condition', 'date_found', 'notes', 'location_id', 'location_name']);
</script>

<template>
    <div class="bike">
        <BikeIcon v-bind:colour="colour" />
        <div class="bike-info">
            <h3>{{ brand }}</h3>
            <div class="condition-container">
                <img alt="gears icon" :src="gears">
                <div class="condition-info">Condition, {{ condition }}</div>
            </div>
            <div class="date-container">
                <img alt="date icon" :src="dateIcon">
                <div class="date-info">Found on {{ date_found }}</div>
            </div>
            <div class="location-container">
                <p>{{ location_name }}</p>
            </div>
            <p>More details...</p>
        </div>
    </div>
</template>


<style scoped>
.bike {
    display: flex;
    align-items: center;
}

.bike-info {
    margin-left: 20px;
}

.condition-container {
    display: flex;
    align-items: center;
    margin-top: 2px;
}

.condition-info {
    margin-left: 10px;
}

.date-container {
    display: flex;
    align-items: center;
    margin-top: 2px;
}

.date-info {
    margin-left: 10px
}
</style>