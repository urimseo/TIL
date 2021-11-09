<template>
  <div>
    <h1>This is parent</h1>
    <p>ParentData: {{ parentData }} </p>
    <input v-model="parentData" type="text" @input="inputParentData">
    <!-- 1. parent 입력창에 input 하면 inputParentData 함수가 실행됨 -->
    <p>appData: {{ appData }}</p>
    <p>ChildData: {{ childData }}</p>
    <Child :appData="appData" :parentData="parentData" 
    @child-input="inputChildData" />
  </div>
</template>

<script>
import Child from './Child.vue'

export default {
  name: 'Parent',
  data: function () {
    return {
      parentData: '',
      childData: '',
    }
  },
  methods: {  
    inputChildData: function (data) { // payload가 이 data에 들어감.
      // console.log('text from child!!')
      this.childData = data
      this.$emit('child-input', this.childData)
    }, // 2. parent-data인풋 이벤트에는 payload칸에 this,parent.Data가 들어가있다
    inputParentData: function () {
      this.$emit('parent-input', this.parentData) 
    }
  },
  props: {
    appData: String,
  },
  components: {
    Child,
  }
}
</script>

<style>

</style>