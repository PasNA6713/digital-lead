<template>
    <v-card height="100px">
      <v-footer
        absolute
        :padless="padless"
      >
        <v-card
          flat
          tile
          width="100%"
          class="black lighten-1 text-center"
        >
          <v-divider></v-divider>
          <v-card-text class="white--text">
            {{ new Date().getFullYear() }} — <strong>MozhaykaTeam</strong>
          </v-card-text>
        </v-card>
      </v-footer>
    </v-card>
</template>

<script>
export default {
    data: () => ({
    padless: false
  })
}
</script>