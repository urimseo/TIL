<template>
  <div>
    <li>
      <img @click="selectVideo" :src="videoImg" alt="">
      <span> {{ videoTitle }}</span>
    </li>
  </div>
</template>

<script>
import _ from 'lodash'

export default { 
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  computed: {
    videoTitle: function () {
      return _.unescape(this.video.snippet.title)
    },
    videoImg: function () {
      return this.video.snippet.thumbnails.default.url
    }
  },
  methods: {
    selectVideo: function() {
      this.$store.dispatch('selectVideo', this.video) // dispatch키워드로 selectVideo라는 액션 부름 
    }
  }
}
</script>

<style>

</style>