<template>
  <div class="layout">
    <el-container>
      <el-header>
          <Header />
      </el-header>
      <el-main>
          <ChatWindow />
          <Credits />
      </el-main>
    </el-container>
  </div>
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
<style>
body {
  background-color: #eee;
  background-image: url(../assets/fond.png);
}
</style>
