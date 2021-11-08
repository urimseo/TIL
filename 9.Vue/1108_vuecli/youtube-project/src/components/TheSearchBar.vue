<template>
  <div>
    <input @keyup.enter = "onInputKeyword" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInputKeyword: function(event) {
      // console.log(event.target.value)
      // 이벤트 발생시키고, 검색어 data 같이넘기기 
      this.$emit('input-change', event.target.value)

    }
  }
}
</script>

<style>

</style>
