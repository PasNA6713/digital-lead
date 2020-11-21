<template>
    <div id="empty-layout">
        <router-view />
    </div>
</template>

<style scoped>
    #empty-layout{
        height: 100%;
        width: 100%;
        background-image: url('../assets/background_empty.jpg');
        background-size: cover;
    }
</style>