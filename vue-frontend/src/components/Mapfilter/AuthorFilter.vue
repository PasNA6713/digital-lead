<template>
    <div class="map-filter">
        <v-card
        class="mx-auto for-filter"
        max-width="344"
        outlined>
        <h4>Фильтр по автору обращения</h4>
            <div class="text-center">
                <v-menu offset-y>
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn
                            color="primary"
                            dark
                            v-bind="attrs"
                            v-on="on"
                        >
                            Dropdown
                        </v-btn>
                    </template>
                    <v-list>
                        <v-list-item
                            v-for="(place, index) in items"
                            :key="index"
                        >
                            <v-list-item-title>{{ place.title }}</v-list-item-title>
                        </v-list-item>
                    </v-list>
                </v-menu>
            </div>
        </v-card>
    </div>
</template>

<script>

export default {
    data: () => ({
    items: [
      { title: 'Click Me' },
      { title: 'Click Me' },
      { title: 'Click Me' },
      { title: 'Click Me 2' },
    ],
  }),
}
</script>

<style scoped>
  .map-filter{
    margin-left: 100px;
  }
  .for-filter{
    padding: 10px 10px;
  }
</style>