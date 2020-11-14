<template>
    <div>
        <br>
        <div class="border primary-border" id="map"></div>
        <br>
    </div>
</template>

<script>
import {mapGetters, mapMutations} from 'vuex'

    export default{
        data: () => ({
            placemarks: {
                "type": "FeatureCollection",
                "features": [
                    {
                        type: 'Feature',
                        id: 3,
                        geometry: {
                            type: 'Point',
                            coordinates: [59.9, 30.55]
                        },
                        properties: {
                            hintContent: 'Содержание всплывающей подсказки',
                            balloonContent: 'Содержание балуна'
                        },
                        options: {
                            preset: "islands#dotIcon",
                            iconColor: "blue"
                        }
                    }   
                ],
            },
            myMap: null,
            objectManager: null,

            messages: null,
            classifier: {
                1: 'yellow',
                2: 'blue',
                3: 'red'
            }
            }),
              methods: {
            ...mapMutations(["updateMessages"])
        },
        computed:{
            
        },

        created() {
            axios
          .get('https://46c60a696609.ngrok.io/message/get/?danger=1')
          .then((response) => {
              this.messages = response.data["data"]
                for (let i=0;i<this.messages.length;i++){
            this.placemarks["features"].push({

            type: 'Feature',
            id: this.messages[i]["id"],
            geometry: {
                type: 'Point',
                coordinates: [this.messages[i]["address"]["latitude"], this.messages[i]["address"]["longtitude"]]
            },
            properties: {
                hintContent: this.messages[i]["date"],
                balloonContent: this.messages[i]["text"]
            },
            options: {
                preset: "islands#dotIcon",
                iconColor: this.classifier[this.messages[i]["danger_level"]]
            }
        })


        }
            this.updateMessages(this.messages)

            ymaps.ready(() => {
                this.myMap = new ymaps.Map("map", {
                    center: [59.9370, 30.3089],
                    zoom: 10,
                    controls: ['zoomControl'], 
                    behaviors: ['drag', 'scrollZoom']
                }, {
                    searchControlProvider: 'yandex#search'
                })

                this.objectManager = new ymaps.ObjectManager({
                    clusterize: true,
                    gridSize: 32,
                    clusterDisableClickZoom: true
                })
                
                this.objectManager.clusters.options.set('preset', 'islands#redClusterIcons')
                this.objectManager.add(this.placemarks)

                this.myMap.geoObjects.add(this.objectManager)


                this.myMap.geoObjects.events.add('click', function (e) {
                    let target = e.get('objectId');
                    const cluster = this.objectManager.clusters.getById(target)
                    if (cluster) {
                        const objects = cluster.properties.geoObjects
                    }
                })
            })
        })
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