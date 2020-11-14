<template>
<div>
    <v-row justify="center">
        <day-statistics />
        <span id="statisticsDivider"></span>
        <month-statistics />
    </v-row>
</div>
</template>

<script>
import DayStatistics from './Day'
import MonthStatistics from './Month.vue'

export default {
    components: {
        DayStatistics,
        MonthStatistics
    }
}
</script>

<style scoped>
    #statisticsDivider{
        width: 400px;
    }
</style>