<template>
    <div>
        <canvas :id="id" width="400" height="400"></canvas>
            <select class="form-control col-4 btn-dark" v-model="chart">
            <option>Час</option>
            <option>День</option>
            <option>Месяц</option>
            <option>Год</option>
        </select>
    </div>
</template>

<script>

export default {
    name: 'chart',

    props: {
        chart: String,
        id: String
    },

    data: () => ({
        labels: '',
        chart_data: '',
        chart_type: ''
    }),

    watch: {
        chart: function(val) {
            this.change_chart(val);
            this.draw_chart();
        }
    },

    methods: {
        draw_chart() {
            var ctx = document.getElementById(this.id).getContext('2d');
            var myChart = new Chart(ctx, {
                type: this.chart_type,
                data: {
                    labels: this.labels,
                    datasets: [{
                        label: this.chart,
                        data: this.chart_data,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(255, 159, 64, 0.2)',
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)',
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });
        },

        change_chart(value) {
            if (value === 'Час') {
                axios(
                    method="POST",
                    url='http://127.0.0.1:8000/message/dashboard/hour/',
                    data = {
                        hour: 1,
                        day: 1,
                        month: 1,
                        year: 2019
                    }
                ).then((response)=>{
                    console.log(response)
                })
                this.chart_type = 'bar';
            }
            if (value === 'День') {
                this.chart_type = 'bar';
            }
            if (value === 'Месяц') {
                this.chart_type = 'bar';
            }
            if (value === 'Год') {
                this.chart_type = 'bar';
            }
        }
    },

    mounted: function() {
        this.change_chart(this.chart);
        this.draw_chart();
    }
}
</script>

<style>

</style>