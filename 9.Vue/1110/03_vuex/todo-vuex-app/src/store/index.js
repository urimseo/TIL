import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    todos: [],
  },
  // state 변경 -> state push하는 함수 여기 작성
  mutations: { 
    CREATE_TODO: function(state, todoItem) { // 대문자로 사용하는 이유: mutations는 state 수정하는 좀 중요한 역할이기 때문에 딱봐도 mutation이라는걸 알 수 있도록 대문자로 표기한다.
      // console.log(todoItem)
      state.todos.push(todoItem) // state 변경
    },
    DELETE_TODO: function(state, todoItem) {
      // 1. todoItme이 첫 번째로 만나는 요소의 index를 가져옴
      const index = state.todos.indexOf(todoItem)
      // 2. 해당 index 1개만삭제하고, 나머지 요소들을 토대로 새로운 배열 생성
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS: function (state, todoItem) {
      state.todos = state.todos.map(todo => {
        if (todo === todoItem) { // 일치하면
          return {
            // title: todoItem.title, // title은 그대로
            // date: new Date(),
            // 전개구문으로 사용
            ...todo, // JS spread syntax
            isCompleted: !todo.isCompleted // 상태를 반대로 토글
            
          }
        } else {
          return todo
        }
      })
    }
  },
  // state를 변경하는 것 외에 다른 모든 동작은 action이 한다.
  actions: { 
    createTodo: function ({ commit }, todoItem) { // context를 통해 store의 모든 속성및 변수에 접근이 가능.
      // console.log(context)
      // console.log(state) // 구조분해 할당으로 인자를 가져와서 사용
      commit('CREATE_TODO', todoItem) // commit 메서드를 통해서 mutation을 호출해서 mutation이 state동작할 수 있도록
    },
    deleteTodo: function ({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodoStatus: function ({ commit }, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
    }
  },
  getters: {
    completedTodosCount: function (state) {
      return state.todos.filter(todo =>{
        return todo.isCompleted === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter(todo =>{
        return todo.isCompleted === false
      }).length
    },
    allTodosCount: function (state) {
      return state.todos.length
    },
  },
  modules: {
  }
})
