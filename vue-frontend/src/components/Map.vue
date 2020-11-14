<template>
    <div>
        <br>
        <div class="border primary-border" id="map"></div>
        <br>
    </div>
</template>

<script>
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
            },
            timeForMap: false
            }),

        created() {
            this.messages = []
            axios
          .get('https://46c60a696609.ngrok.io/message/get/')
          .then((response) => {
              this.messages = response
                console.log()
                for (let i=0;i<this.messages.length;i++){
            console.log("circle")
            this.placemarks["features"].push({
            type: 'Feature',
            id: this.messages["data"][i]["id"],
            geometry: {
                type: 'Point',
                coordinates: [this.messages["data"][i]["address"]["longtitude"], this.messages["data"][i]["address"]["latitude"]]
            },
            properties: {
                hintContent: this.messages["data"][i]["date"],
                balloonContent: this.messages["data"][i]["text"]
            },
            options: {
                preset: "islands#dotIcon",
                iconColor: this.classifier[this.messages["data"][i]["danger_level"]]
            }
        })
        }
            console.log("ym")
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
    height: 600px;
    margin-left: 50px;
}
</style>