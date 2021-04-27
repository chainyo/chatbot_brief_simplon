<template>
  <Header />
  <ChatWindow />
  <Credits />
</template>

<script>
import ChatWindow from '@/components/ChatWindow'
import Credits from '@/components/Credits'
import Header from '@/components/Header'

export default {
  name: 'ChatBot',
  components: {
    ChatWindow,
    Credits,
    Header
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
