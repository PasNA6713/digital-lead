<template>
  <div>
    <danger-filter />
    <br>
    <author-filter />
  </div>
</template>

<script>
import DangerFilter from './DangerFilter'
import AuthorFilter from './AuthorFilter'

export default {
  components: {
    DangerFilter,
    AuthorFilter
  }
}
</script>

<style scoped>
  .checkbox-filter{
    margin-left: 100px;
  }
  .for-filter{
    padding: 10px 10px;
  }
</style>