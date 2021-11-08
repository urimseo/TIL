<template>
    <div>
      <h1>점심메뉴</h1>
      <button @click="getLunchMenu">Pick Lunch</button>
      <p>{{ selectedLunch }}</p>
      <br>
      <br>
      <h3>로또를 뽑아보자</h3>
      <button @click="moveToLotto">Pick Lotto</button>
    </div>
</template>

<script>
  import _ from 'lodash'

  export default {
    name: 'TheLunch',
    data: function () {
      return { 
        lunch: ['타코', '스시', '샌드위치', '케이크'],
        selectedLunch : '',
      }
    },
    methods: {
      getLunchMenu: function () {
        this.selectedLunch = _.sample(this.lunch)
      },
      moveToLotto: function () {
        this.$router.push({ name: 'TheLotto',params: {lottoNum: 6} })
      }
    }
  }
</script>
