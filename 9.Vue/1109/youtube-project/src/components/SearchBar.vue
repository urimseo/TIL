<template>
  <div>
    <input @keypress.enter="onInputKeyword" type="text">


  </div>
</template>

<script>
export default {
  name: 'Searchbar',
  methods: {
    onInputKeyword: function (event) {
      // console.log(event.target.value)
      this.$emit('input-search', event.target.value) // 데이터 하나 더 넘기고 싶으면 그냥 ,해서 추가하면됨 -> App.vue 에서 매개변수 하나 추가 
    }
  }
}
</script>

<style>

</style>