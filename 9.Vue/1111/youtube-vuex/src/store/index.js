import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https:/www.googleapis.com/youtube/v3/search'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    searchResult: [],
    selectedVideo: null,
  },
  mutations: {
    ADD_SEARCH_RESULT: function (state, items) {
      state.searchResult = items
    },
    SELECT_VIDEO: function (state,video) {
      state.selectedVideo = video
    }
  },
  actions: {
    onSearch: function ({ commit }, query) { // {commit} = context.commit
      axios.get(API_URL, {
        params: {
          part: 'snippet',
          q: query, 
          key: API_KEY,
          type: 'video',
        }
      })
        .then(res => {
          commit('ADD_SEARCH_RESULT', res.data.items)
        })
        .catch(err => {
          console.log(err)
        })
    },

    selectVideo: function ({commit}, video) {
      commit('SELECT_VIDEO', video) // vue에서 부르면 이제 위의 mutation으로 함수호출
    }
  },
  // 중앙저장소에 미리 계산해두고 계산된것 가져다가 쓰는 용도.
  getters: {
    // 선택된 비디오가 있는지 확인하가
    isSelected: function(state) {
      return state.selectedVideo != null
    },
    // Video URL 만들기
    videoUrl: function(state) {
      if (state.selectedVideo) {
        const videoId = state.selectedVideo.id.videoId
        return `https://www.youtube.com/embed/${videoId}`
      }
      return ''
    },
    // 선택된 비디오 제목 리턴하기
    videoTitle: function (state) {
      if (state.selectedVideo) {
        const title = state.selectedVideo.snippet.title
        return _.unescape(title)
      }
      return ''
    },
    // 비디오 상세 설명 
    videoDesc: function (state) {
      if (state.selectedVideo) {
        const desc = state.selectedVideo.snippet.description
        return _.unescape(desc)
      }
      return ''
    }

  },
  modules: {
  },

})
