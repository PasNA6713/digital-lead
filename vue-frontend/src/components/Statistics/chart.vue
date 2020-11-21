<template>
  <div class="my-app">
    
    <D3BarChart
      :config="chart_config"
      :datum="to_chart"
    ></D3BarChart>
    

    <div class="text-center">
    <v-btn
      rounded
      color="primary"
      dark
      v-model="value"
      @click="change_chart(value[0])"
    >
      Час
    </v-btn>

    <v-btn
      rounded
      color="primary"
      dark
      v-model="value"
      @click="change_chart(value[1])"
    >
      День
    </v-btn>

    <v-btn
      rounded
      color="primary"
      dark
      v-model="value"
      @click.prevent="change_chart(value[2])"
    >
      Месяц
    </v-btn>

    <v-btn
      rounded
      color="primary"
      dark
      v-model="value"
      @click="change_chart(value[3])"
    >
      Год
    </v-btn>
  </div>

  </div>
</template>

<script>
    import Vue from 'vue'
    import { D3BarChart } from 'vue-d3-charts';

    export default {
        name: 'chart',
        props: {
            datum: Array,
        },
        

    components: {
        D3BarChart,
    },

    data() {
        return {
        to_chart: [
            {"dtp":7, "year":0},
            {"dtp":12, "year":5},
            {"dtp":1, "year":10},
            {"year":15, "dtp":5},
            {"year":20,"dtp":1},
            {"year":25,"dtp":1},
            {"year":30,"dtp":2},
            {"year":35,"dtp":2},
            {"year":40,"dtp":0},
            {"year":45,"dtp":1},
            {"year":50,"dtp":1},
            {"year":55,"dtp":1}
        ],
        chart_config: {
            key: 'year',
            values: ['dtp']
        },
        count: 2010,
        value: ["Час", "День", "Месяц", "Год"],
        resp: null
        }
    },
    methods: {
        change_chart(value) {
            if (value === 'Час') {
                axios.post('https://748f90e2a605.ngrok.io/message/dashboard/hour/', {
                    hour: 1,
                    day: 1,
                    month: 1,
                    year: 2019
                }).then((response)=>{
                    Vue.set(this.$data, 'resp', response.data)
                    let i = null
                    this.to_chart = []
                    for (i in this.resp) {
                        // console.log("i", i)
                        // console.log("push", this.resp[i])
                        this.to_chart.push({
                            dtp: this.resp[i],
                            year: i
                        })
                    }
                    console.log(this.to_chart)
                })
            }
            if (value === 'День') {
                axios.post('https://748f90e2a605.ngrok.io/message/dashboard/day/', {
                    day: 1,
                    month: 1,
                    year: 2019
                }).then((response)=>{
                    Vue.set(this.$data, 'resp', response.data)
                    let i = null
                    this.to_chart = []
                    for (i in this.resp) {
                        // console.log(i)
                        // console.log(this.resp[i])
                        this.to_chart.push({
                            dtp: this.resp[i],
                            year: i
                        })
                    }
                })
            }
            if (value === 'Месяц') {
                axios.post('https://748f90e2a605.ngrok.io/message/dashboard/month/', {
                    month: 1,
                    year: 2019
                }).then((response)=>{
                    Vue.set(this.$data, 'resp', response.data)
                    let i = null
                    this.to_chart = []
                    for (i in this.resp) {
                        // console.log(i)
                        // console.log(this.resp[i])
                        this.to_chart.push({
                            dtp: this.resp[i],
                            year: i
                        })
                    }
                })
            if (value === 'Год') {
                axios.post('https://748f90e2a605.ngrok.io/message/dashboard/year/', {
                    year: 2019
                }).then((response)=>{
                    Vue.set(this.$data, 'resp', response.data)
                    let i = null
                    this.to_chart = []
                    for (i in this.resp) {
                        // console.log(i)
                        // console.log(this.resp[i])
                        this.to_chart.push({
                            dtp: this.resp[i],
                            year: i
                        })
                    }
                })
            }
        }
    }
}
}
</script>
