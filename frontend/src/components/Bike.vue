<script setup>
defineProps(['id', 'brand', 'colour', 'condition', 'date_found', 'notes', 'location_id'])
</script>

<template>
    <h4>{{ brand }}, {{ colour }}, {{ condition }}, {{ date_found }}, {{ notes }}</h4>
</template>