<template>
  <div id="app">
    <h1>About</h1>
    <h2>{{ myMessage }}</h2>
    <h2>{{ parentData }}</h2>
    <input 
    type="text"
    @keyup.enter="childInputChange"
    >
  </div>
</template>

<script>
export default {
  name: 'About',
  data: function() {
    return {
      childInputData: null,
    }
  },
  props: {
    myMessage: String,
    parentData: String,
  },
  methods: {
    childInputChange: function() {
      this.$emit('child-input-change', this.childInputData)
    }
    // emit 메서드를 활용하여 child-input-change라는 이벤트를 발생시킬건데, 
    // 데이터는 childInputData를 보내서 발생시킨다!
  }
}
</script>

<style>

</style>