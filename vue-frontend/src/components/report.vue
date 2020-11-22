<template>
    <v-card class="mr-3 pb-3">
        <v-card-title justify="space-between">{{data.name}}</v-card-title>
        <span style="position: absolute; right: 20px; top: 10px;">{{data.date}}</span>
        <v-card-text>{{data.text}}</v-card-text>
        <v-btn style="position: absolute; right: 20px; bottom: 10px;"
            class="mx-2"
            fab
            dark
            small
            color="#F58D8E"
        >
            {{data.likes}}
            <v-icon dark>
            mdi-heart
            </v-icon>
        </v-btn>
    </v-card>
</template>

<script>
export default {
    proprs: ['data'],

    mounted() {
        console.log(this.data)
    }
}
</script>