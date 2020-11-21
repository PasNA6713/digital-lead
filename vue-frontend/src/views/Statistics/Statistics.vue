<template>
<div>
        <chart />
    <v-row justify="center">
        <day-statistics />
        <span id="statisticsDivider"></span>
        <month-statistics/>
    </v-row>
        <br>
</div>
</template>

<script>
import DayStatistics from './Day'
import MonthStatistics from './Month.vue'
import Vue from 'vue'
import chart from '../../components/Statistics/chart.vue'

export default {
    data() {
        return {
                to_chart: [],
                resp: null
        }
    },

    components: {
        DayStatistics,
        MonthStatistics,
        chart
    },
}
</script>

<style scoped>
    #statisticsDivider{
        width: 400px;
    }
</style>