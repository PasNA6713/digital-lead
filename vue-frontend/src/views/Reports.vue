<template>
    <div>
        <v-row>
            <v-col cols="3">
                <div class="menu">
                    <v-col>
                        <a v-bind:class="{ 'red--text': isActive1 }" @click.prevent="getComplaints">Мои жалобы</a>
                    </v-col>
                    <v-col>
                        <a v-bind:class="{ 'red--text': isActive2 }" @click.prevent="getOffers">Мои предложения</a>
                    </v-col>
                    <v-col>
                        <a>Избранное</a>
                    </v-col>
                </div>
            </v-col>
            <v-col cols="8" class="p-3 pr-6">
                <report :isLikable="false" v-for="i in reports" :key="i.text" :data="i"/>
            </v-col>
        </v-row>
    </div>
</template>

<script>
import report from '../components/report.vue'

export default {
    components: {
      report
    },
    data: () => ({
        reports: [],
        isActive1: true,
        isActive2: false
    }),

    mounted() {
        axios({
            method: 'GET',
            url: 'https://fc9752e33a86.ngrok.io/message/get/?event=T&author=6'
        }).then(response => {
            this.reports = response.data.data
        })
    },
    methods: {
        getComplaints(){
            this.isActive1 = true
            this.isActive2 = false
            axios({
            method: 'GET',
            url: 'https://fc9752e33a86.ngrok.io/message/get/?event=T&author=6'
        }).then(response => {
            this.reports = response.data.data
        })
        },
        getOffers(){
            this.isActive1 = false
            this.isActive2 = true
            axios({
            method: 'GET',
            url: 'https://fc9752e33a86.ngrok.io/message/get/?event=Y&author=6'
        }).then(response => {
            this.reports = response.data.data
        })
        }
    }
}
</script>

<style scoped>
    a{
        font-family: Century Gothic;
        font-size: 30px;
        line-height: 25px;
        padding-bottom: 40px;
        font-weight: 900;
        padding-top: 30px;
    }
    .menu{
        padding-top: 80px;
        padding-left: 60px;
    }
    .report-msg{
        margin-bottom: 30px;
    }
    .divider{
        margin-top: 50px;
    }
</style>
