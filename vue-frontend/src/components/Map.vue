<template>
    <div>
        <br>
        <v-row>
            <v-col cols="4">
                <yandex-map  id="map"
                    :settings="settings"
                    :coords="mapCenter"
                    :zoom="10" 
                    :use-object-manager="true"
                    :controls="['zoomControl']"
                    @click.prevent="onClick"
                    @map-was-initialized="getMapInstance"
                >
                </yandex-map>
            </v-col>
            <v-col cols="6" class="p-2 pr-7 report-col" v-if="isShow">
                <report class="report-msg"
                v-for="(report, index) in reports"
                :key="index"
                :data="reports[index]"
                />
                <!-- <v-pagination
                    v-model="page"
                    :length="76"
                    :total-visible="7"
                ></v-pagination> -->
            </v-col>
        </v-row>
        <br>
    </div>
</template>

<script>
    import { yandexMap, ymapMarker } from 'vue-yandex-maps'
    import dataset from '../assets/dataset.json'
    import Report from '../components/report.vue'

    export default{
        props: ["isNeedRefresh", "dynamicFilter"],
        components: {
            yandexMap, 
            ymapMarker,
            Report
        },

        data: () => ({
            settings: {
                apiKey: 'e70694c3-ce7f-4459-b7f6-be3d53e2cc8e',
                lang: 'ru_RU',
                coordorder: 'latlong',
                version: '2.1'
            },
            mapCenter: [59.9370, 30.3089],
            isShow: false,
            filter: [],
            currentMap: null,
            objectManager: null,
            placemarks: [],

            classifier: {
                1: 'yellow',
                2: 'blue',
                3: 'red'
            },
            classes: [
                'Дтп',
                'Пожар',
                'Свалка',
                'Загрязнение водоемов',
                'Дороги',
                'Благоустройство домов',
                'Благоустройство дворов',
                'Благоустройство придомовых территорий',
                'Нарушение водоснабжения',
                'Нарушение электроснабжения'
            ],
            reports: [
                {
                    name: 'Пастухов Никита',
                    date: '22.11.2020',
                    text: 'На ул. Тотмина города Тосно дорожное покрытие частично отсутствует, отсутствует дренаж, пешеходные тротуары, плиты разбиты, торчит арматура, асфальт в выбоинах и ямах.',
                    likes: '127'
                }
                // {
                //     name: 'Алексей Иванов',
                //     date: '21.11.2020',
                //     text: 'Состояние железнодорожного переезда не соответствует никаким нормам!!! Ямы местное население вынуждено закладывать кирпичами. На мое телефонное обращение никакой реакции не последовало. Проблема никак не решается в течении нескольких лет. В летний период замедленный проезд данного переезда приводит к многочасовым пробкам!',
                //     likes: '234'
                // },
                // {
                //     name: 'Евгения Малышева',
                //     date: '20.11.2020',
                //     text: 'Здравствуйте!Уже не первый раз пишем жалобы в управляющую компанию \"Солнечный\" об отвратительной уборке. Невозможно выехать из двора, пройти с коляской, я уже молчу о пожилых людях, которым очень тяжело пройти. Перестали посыпать песком, хотя вокруг много домов строится и песка точно много. Около самого управления конечно же чисто, а чем хуже мы? Мы платим деньги и при этом постоянно пишем про ужасную уборку, ходим жалуемся. Очень просим помочь, чтобы уборка была надлежащей!',
                //     likes: '366'
                // }
            ],
            page: 1,
        }),

        methods: {
            onClick(e) {
                this.isShow = true
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
                            this.currentMap.geoObjects.events.add('click', this.onClick)
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
        // Получение json (запрос на сервер) и преобразование в валидные марк/еры для карты
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
        },
    }
}
</script>

<style scoped>
    #map{
        width: 800px; 
        height: 800px;
        margin-left: 60px;
    }
    .report-col{
        margin-left: 300px;
    }
    .report-msg{
        margin-bottom: 30px;
    }
</style>

