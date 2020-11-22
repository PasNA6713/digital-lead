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
        </yandex-map>
        <br>
    </div>
</template>

<script>
    import { yandexMap, ymapMarker } from 'vue-yandex-maps'
    import dataset from '../assets/dataset.json'

    export default{
        props: ["isNeedRefresh", "dynamicFilter"],
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

            filter: [],
            currentMap: null,
            objectManager: null,
            placemarks: [],

            classifier: {
                1: 'yellow',
                2: 'blue',
                3: 'red'
            },
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
                this.$emit('for-autocomplete', this.filter)
            }
        }
    },
    mounted(){
        // Получение json (запрос на сервер) и преобразование в валидные маркеры для карты
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
            this.filter.push(
                {
                    "id": dataset[i]["id"],
                    "district": dataset[i].address["district"],
                    "event_class": dataset[i]["event_class"],
                    "date": dataset[i]["date"]
                })
        }

    },

    watch: {
        isNeedRefresh: function(newIsNeedRefresh, oldIsNeedRefresh){
            if (newIsNeedRefresh){
                
                let myFilter = this.dynamicFilter
                let filteredPlacemarks = []
                
                if (myFilter[0].length == 0){
                    for(let i=0;i<this.filter.length;i++)
                    {
                        myFilter[0].push(this.filter[i]["district"])
                    }
                }

                if (myFilter[1].length == 0){
                    for(let i=0;i<this.filter.length;i++)
                    {
                        myFilter[1].push(this.filter[i]["date"])
                    }
                }

                if (myFilter[2].length == 0){
                    for(let i=0;i<this.filter.length;i++)
                    {
                        myFilter[2].push(this.filter[i]["event_class"])
                    }
                }

                // Предусмотреть повторный запрос на сервер или так и оставить из локальных данных
                for (let i=0;i<dataset.length;i++){
                    if (myFilter[0].includes(dataset[i].address["district"]) && 
                        myFilter[1].includes(dataset[i]["date"]) &&
                        myFilter[2].includes(dataset[i]["event_class"])){
                            console.log("here")
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
                        filteredPlacemarks.push(mapMarker)
                    }
                }

                //console.log("filteredPlacemarks", filteredPlacemarks)
                
                this.objectManager.removeAll()
                this.objectManager.add(filteredPlacemarks)
                
                this.$emit('refreshed')
            }
        }
    }
}
</script>

<style scoped>
#map{
    width: 400px; 
    height: 400px;
    margin-left: 60px;
}
</style>
