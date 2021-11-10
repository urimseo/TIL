<template>
  <div>
    <input 
      type="text"
      v-model.trim="todoTitle"
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo: function () { // MUTATION을  호출하는 메서드는 commit
      const todoItem = {
        title: this.todoTitle,
        isCompleted: false,
        date: new Date().getTime()
      }
      // this.$store.commit('CREATE_TODO', todoItem) // mutation 호출 -> commit('호출 mutations', payload(전달할 데이터)) - actions가 없었기 떄문에 임의로 여기서 한것
      if (todoItem.title) {
        this.$store.dispatch('createTodo', todoItem) // actions 호출
      }
      this.todoTitle = null // push이후 검색창 reset
    }
  }

}
</script>

<style>

</style>