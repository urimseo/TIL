<template>
  <div>
    <h2>점심메뉴추천</h2>
    <button @click="pickOneInLunchMenu">점뭐먹</button>
    <h2>점심은?: {{ selectedLunchMenu }}</h2>
    <input v-model='lottoNum' placeholder="로또 번호 추천 개수 입력" type="text">
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data: function () {
    return  {
      lunch: ['국밥', '짜장면', '햄버거'],
      selectedLunchMenu: '',
      lottoNum: 0,
    }
  },
  methods: {
    pickOneInLunchMenu: function () {
      const randomIndex = _.random(this.lunch.length-1)
      this.selectedLunchMenu = this.lunch[randomIndex]

      // redirect
      // this.$router.push('/lotto')
      this.$router.push({ name: 'TheLotto',params: { lottoNum: this.lottoNum }})

    },

  }
}
</script>

<style>

</style>