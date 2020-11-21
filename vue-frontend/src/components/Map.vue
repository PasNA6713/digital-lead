<template>
    <div>
        <br>
        <yandex-map  id="map"
            :settings="settings"
            :coords="mapCenter"
            :zoom="10" 
            :use-object-manager="true"
            @click="onClick"
        >
            <ymap-marker 
            :key="marker.id"
            v-for="marker in placemarks" 
            :coords="marker.coords" 
            marker-id="marker.id" 
            hint-content="marker.id"
            />
        </yandex-map>
        <br>
    </div>
</template>

<script>
    import { yandexMap, ymapMarker } from 'vue-yandex-maps'

    export default{
        components: {
            yandexMap, 
            ymapMarker
        },
        data: () => ({
            settings: {
                apiKey: 'e70694c3-ce7f-4459-b7f6-be3d53e2cc8e',
                lang: 'ru_RU',
                coordorder: 'latlong',
                version: '2.1'
            },
            // isObjectManager: true,
            mapCenter: [59.9370, 30.3089],
            placemarks: 
                [
                    {
                        "id": 1,
                        "coords": [59.9, 30.55]
                    },
                    {
                        "id": 2,
                        "coords": [59.945800, 30.271400]
                    },
                    {
                        "id": 3,
                        "coords": [59.945800, 30.271000]
                    }
                ],
            classifier: {
                1: 'yellow',
                2: 'blue',
                3: 'red'
            }
            }),
        methods: {
            onClick(e) {
                this.placemarks = e.get('coords');
        }
    }
}
</script>

<style scoped>
#map{
    width: 800px; 
    height: 660px;
    margin-left: 30px;
}
</style>