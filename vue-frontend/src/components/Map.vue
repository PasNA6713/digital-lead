<template>
    <div>
        <br>
        <yandex-map  id="map"
            :settings="settings"
            :coords="mapCenter"
            :zoom="10" 
            :use-object-manager="true"
            :controls="['zoomControl']"
            @map-was-initialized="getMapInstance"
        >
            <!-- <ymap-marker 
            :key="marker.id"
            v-for="marker in placemarks" 
            :coords="marker.coords" 
            marker-id="marker.id" 
            hint-content="marker.id"
            @click="onClick"
            /> -->
        </yandex-map>
        <br>
    </div>
</template>

<script>
    import { yandexMap, ymapMarker } from 'vue-yandex-maps'
    import dataset from '../assets/dataset.json'

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
            mapCenter: [59.9370, 30.3089],

            currentMap: null,
            objectManager: null,
            placemarks: [],

            classifier: {
                1: 'yellow',
                2: 'blue',
                3: 'red'
            }
        }),

        methods: {
            onClick(e) {
                this.placemarks = e.get('coords');
        },
            async getMapInstance(map) {
                if (map) {
                try {
                    this.currentMap = map
                    this.objectManager = new ymaps.ObjectManager({
                                clusterize: true,
                                gridSize: 32,
                                clusterDisableClickZoom: true
                            })
                        try {
                            this.objectManager.add(this.placemarks)
                            this.currentMap.geoObjects.add(this.objectManager)
                        } catch (error) {
                            console.log('no placemarks!')
                        }
                        
                } catch (error) {
                    console.log(error)
                }
            }
        }
    },
    mounted(){
        // Получение json и преобразование в валидные маркеры для карты
        for (let i=0;i<dataset.length;i++){
            let mapMarker = {
                            type: 'Feature',
                            id: dataset[i]["id"],
                            geometry: {
                                type: 'Point',
                                coordinates: [dataset[i]["address"]["latitude"], dataset[i]["address"]["longtitude"]]
                            },
                            properties: {
                                hintContent: dataset[i]["date"],
                                balloonContent: dataset[i]["text"]
                            },
                            options: {
                                preset: "islands#dotIcon",
                                iconColor: this.classifier[dataset[i]["danger_level"]]
                            }
            }
            this.placemarks.push(mapMarker)
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