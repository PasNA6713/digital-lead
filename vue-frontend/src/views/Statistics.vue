<template>
<div>
    <v-row justify="center">
        <v-col cols="4">
            <districts :states="dist" label="Укажите свой район"/>
            <districts :states="classes" label="Выберите класс происшествия"/>

            <day-statistics class="ml-2"/>
        </v-col>

        <v-col cols="8">
            <chart />
        </v-col>
    </v-row>
</div>
</template>

<script>
import Vue from 'vue'
import DayStatistics from '../components/Statistics/DailyCalendar.vue'
import chart from '../components/Statistics/custom_chart.vue'
import districts from '../components/autocomplete.vue'

export default {
    data() {
        return {
            dist: [
                'Выборгский район',
                'Московский район',
                'Петродворцовый район',
                'Курортный район',
                'Приморский район',
                'Пушкинский район',
                'Петроградский район',
                'Василеостровский район',
                'Красносельский район',
                'Невский район',
                'Центральный район',
                'Адмиралтейский район',
                'Фрунзенская район',
                'Калининский район',
                'Кировский район',
                'Кронштадтский район',
                'Колпинский район',
                'Красногвардейский район'
            ],

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
            ]
        }
    },

    components: {
        DayStatistics,
        districts,
        chart
    },
}
</script>

<style scoped>
</style>