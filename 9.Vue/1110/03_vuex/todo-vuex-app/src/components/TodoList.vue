<template>
  <div>
    <todo-list-item 
      v-for="todo in todos"
      :key="todo.date"
      :todo="todo"
    ></todo-list-item>
  </div>

</template>

<script>
import { mapState } from 'vuex'
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  // 1. 기본 구조
  // computed: {
  //   todos: function () {
  //     return this.$store.state.todos
  //   },
  // },

  // 2. mapState
  // computed: mapState([
  //   'todos',
  // ]),
  // 3. 객체 전개 연산자로 여러개 mapping
  computed: {
    // 여기에 다른 state값을 넣을 수 있다. 
    // 객체전개형태로...
    ...mapState([
      'todos',
    ])
  }

}
</script>

<style>

</style>