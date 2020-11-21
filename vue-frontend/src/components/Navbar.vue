<template>
    <div>
      <v-toolbar
        dark
        prominent
        :collapse="collapseOnScroll"
      >
        <v-toolbar-title class="toolbar-title">SPb-ALERT</v-toolbar-title>
        <NavbarButtons />
        <v-spacer></v-spacer>
    
        <v-btn icon>
        <!-- <router-link to="/login" class="no-link-decoration"> -->
            <v-icon>mdi-account</v-icon>
        <!-- </router-link> -->
        </v-btn>

        <v-btn icon>
        <a @click.prevent="logout" class="no-link-decoration">
            <v-icon>mdi-export</v-icon>
        </a>
        </v-btn>

      </v-toolbar>
    </div>
</template>

<style scoped>
    .no-link-decoration{
        text-decoration: none;
        color: white;
    }
    .toolbar-title{
        font-weight: 300;
        font-family: sans-serif;
        size: 6rem;
        letter-spacing: -.015625em;
        margin-bottom: 41px;
    }
</style>

<script>
import NavbarButtons from './NavbarButtons'

export default {
    name: 'Navbar',
    data: () => ({
    collapseOnScroll: false,
  }),
    components: {
        NavbarButtons
    },
  methods: {
    logout(){
      this.$router.push('/login?message=logout')
    }
  }
}
</script>