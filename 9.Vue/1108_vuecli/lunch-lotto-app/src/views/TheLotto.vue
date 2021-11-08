<template>
  <div>
    <h1>로또</h1>
    <button @click="getLuckyNum">Click Lucky Numbers</button>
    <p>{{ selectedLuckyNum }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: "TheLotto",
    data: function() {
      return{
        selectedLuckyNum: '',
      }
    },
    methods: {
      getLuckyNum: function() {
        const numbers = _.range(1, 46)
        this.selectedLuckyNum = _.sampleSize(numbers, this.$route.params.lottoNum)
      }
    }
}
</script>

<style>

</style>