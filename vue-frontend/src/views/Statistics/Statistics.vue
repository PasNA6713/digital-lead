<template>
<div>
    <v-row justify="center">
        <day-statistics />
        <span id="statisticsDivider"></span>
        <month-statistics/>

        <chart id="four" chart='Час'/>
    </v-row>
</div>
</template>

<script>
import DayStatistics from './Day'
import MonthStatistics from './Month.vue'
import chart from '../../components/Statistics/chart.vue'

export default {
    components: {
        DayStatistics,
        MonthStatistics,
        chart
    }
}
</script>

<style scoped>
    #statisticsDivider{
        width: 400px;
    }
</style>