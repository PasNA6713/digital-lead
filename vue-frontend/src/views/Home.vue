<template>
    <div>
        <v-row>
        <Map />
        <map-filter />
        </v-row>
    </div>
</template>

<script>
import Map from '../components/Map'
import MapFilter from '../components/Mapfilter/MapFilter'

export default {
    components: {
        Map,
        MapFilter
    }
}
</script>