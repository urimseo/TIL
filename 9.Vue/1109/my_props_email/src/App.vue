<template>
  <div id="app">
    <!-- 사용한다  -->
    <h1>App</h1>
    <p>Appdata: {{ appData }}</p>
    <input v-model="appData" type="text">
    <p>ParentData: {{ parentData }}</p>
    <p>ChildData: {{ childData }}</p>
    <Parent :appData="appData"
    @parent-input="inputParent"  
    @child-input="inputChild" />
<!-- Parent에서 보낸 신호를 @parent-input이 받아서 inputParent함수 실행 -->
  </div>
</template>

<script>
// 1. 불러온다 (import)
import Parent from './components/Parent.vue'

  // 2. 등록한다 
export default {
  name: 'App', 
  components: {
    Parent,
  },
  data: function () {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  }, 
  // 실행할 함수에서 데이터를 저장 
  methods: {
    inputParent: function (data) { // payload안에 담겨있는 data를 parentData에 넣기
      this.parentData = data
    }, 
    inputChild: function (data) {
      this.childData = data
    }
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
