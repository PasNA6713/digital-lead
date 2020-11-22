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
      class="mx-2"
    >
      Час
    </v-btn>

    <v-btn
      rounded
      color="primary"
      dark
      v-model="value"
      @click="change_chart(value[1])"
      class="mx-2"
    >
      День
    </v-btn>

    <v-btn
      rounded
      color="primary"
      dark
      v-model="value"
      @click.prevent="change_chart(value[2])"
      class="mx-2"
    >
      Месяц
    </v-btn>

    <v-btn
      rounded
      color="primary"
      dark
      v-model="value"
      @click.prevent="change_chart('Год')"
      class="mx-2"
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
            {"messages":7, "year":0},
            {"messages":12, "year":5},
            {"messages":1, "year":10},
            {"year":15, "messages":5},
            {"year":20,"messages":1},
            {"year":25,"messages":1},
            {"year":30,"messages":2},
            {"year":35,"messages":2},
            {"year":40,"messages":0},
            {"year":45,"messages":1},
            {"year":50,"messages":1},
            {"year":55,"messages":1}
        ],
        chart_config: {
            key: 'year',
            values: ['messages']
        },
        count: 2010,
        value: ["Час", "День", "Месяц", "Год"],
        resp: null
        }
    },
    methods: {
        change_chart(value) {
            if (value === 'Час') {
                axios.post('http://127.0.0.1:8000/message/dashboard/hour/', {
                    hour: 19,
                    day: 21,
                    month: 7,
                    year: 2020
                }).then((response)=>{
                    Vue.set(this.$data, 'resp', response.data)
                    let i = null
                    this.to_chart = []
                    for (i in this.resp) {
                        this.to_chart.push({
                            messages: this.resp[i],
                            year: i
                        })
                    }
                })
            }
            if (value === 'День') {
                axios.post('http://127.0.0.1:8000/message/dashboard/day/', {
                    day: 21,
                    month: 7,
                    year: 2020
                }).then((response)=>{
                    Vue.set(this.$data, 'resp', response.data)
                    let i = null
                    this.to_chart = []
                    for (i in this.resp) {
                        this.to_chart.push({
                            messages: this.resp[i],
                            year: i
                        })
                    }
                })
            }
            if (value === 'Месяц') {
                axios.post('http://127.0.0.1:8000/message/dashboard/month/', {
                    month: 7,
                    year: 2020
                }).then((response)=>{
                    Vue.set(this.$data, 'resp', response.data)
                    let i = null
                    this.to_chart = []
                    for (i in this.resp) {
                        this.to_chart.push({
                            messages: this.resp[i],
                            year: i
                        })
                    }
                })
            if (value === 'Год') {
                axios.post('http://127.0.0.1:8000/message/dashboard/year/', {
                    year: 2020
                }).then((response)=>{
                    Vue.set(this.$data, 'resp', response.data)
                    let i = null
                    this.to_chart = []
                    for (i in this.resp) {
                        this.to_chart.push({
                            messages: this.resp[i],
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
