<template>
  <div>
    <input 
      type="text" 
      v-model.trim="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createTodo: function () {
      const todoItem = {
        title: this.title,
      }

      if (todoItem.title) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/todos/',
          data: todoItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            // 작성하고나면 TodoList로 바로 이동될 수 있도록 하기 -> created hook 넣어놔서 가능!
            this.$router.push({ name: 'TodoList' })
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
  }
}
</script>
