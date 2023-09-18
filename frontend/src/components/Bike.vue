<script setup>
import BikeIcon from './BikeIcon.vue';
defineProps(['id', 'brand', 'colour', 'condition', 'date_found', 'notes', 'location_id']);
</script>

<template>
    <BikeIcon v-bind:colour="colour" />
    <h4>{{ brand }}, {{ condition }}, {{ date_found }}</h4>
    <p>More details...</p>
</template>