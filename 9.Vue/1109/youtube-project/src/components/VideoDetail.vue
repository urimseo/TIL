<template>
  <div v-if="video">
    <iframe :src="videoURL" frameborder="0"></iframe>
    <h2> {{ video.snippet.title | stringUnescape }}</h2>
    <p> {{ video.snippet.description | stringUnescape }}</p>
    
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: [String, Object] // 2개를 지정하는 이유: 처음에 아무것도 안고른 경우 빈 문자열.. 클릭해서 넘겨줘야 object가 넘어간다.
    }
  },
  computed: {
    videoURL: function () {
      const videoId = this.video.id.videoId
      return `http://www.youtube.com/embed/${videoId}`
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>

</style>