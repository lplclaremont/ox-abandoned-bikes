<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
    <main>
        <RouterView />
    </main>
</template>


<style>
body, html {
    margin: 0;
    padding: 0;
    height: 100%;
}

main {
    background-color: rgb(167, 209, 241);   
}

#app {
    margin: 0;
    padding: 0;
}
</style>
