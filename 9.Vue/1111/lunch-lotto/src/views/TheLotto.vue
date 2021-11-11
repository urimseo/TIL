<template>
  <div>
    <h2>로또번호 추첨</h2>
    <button @click="getLuckyNums">Get Lucky Number</button>
    <p>로또추첨번호 {{ $route.params.lottoNum}}개</p>
    <ul>
      <li v-for="(num, index) in selectedLuckyNums" :key="index">{{ num }}</li>
      
    </ul>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data: function () {
    return {
      selectedLuckyNums: [],
      
    }
  },
  methods: {
    getLuckyNums: function () {
      const numbers = _.range(1, 46)
      this.sampleNums = _.sampleSize(numbers,this.$route.params.lottoNum)
      this.selectedLuckyNums = _.sortBy(this.sampleNums)
    }
  }
}
</script>

<style>

</style>