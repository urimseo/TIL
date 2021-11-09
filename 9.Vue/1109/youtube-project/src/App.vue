<template>
  <div id="app">
    <h1>My First Youtube Project</h1>
    <SearchBar @input-search="onInputSearch" />
    <VideoDetail :video="selectedVideo"/>
    <VideoList :videos="videos" @select-video="onVideoSelect" />
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'


const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data: function () {
    return {
      inputValue: '',
      videos: [],
      selectedVideo: '',
    }
  },
  methods: {
    onInputSearch: function (inputText) {
      // console.log('데이터가 searchbar로부터 올라옴')
      // console.log(inputText)
      this.inputValue = inputText
      
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: this.inputValue
      }

      axios.get(API_URL, {
        params,
      })
        .then((res) => {
          this.videos = res.data.items
          if (!this.selectedVideo) {
            // 만약 선택된 영상이 없다면 맨 처음 동영상이 default 값으로 뜰 수 있도록 설정.
            this.selectedVideo = this.videos[0]
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    onVideoSelect: function (video) {
      this.selectedVideo = video

    },

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
