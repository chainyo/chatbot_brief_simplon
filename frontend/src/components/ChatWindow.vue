<template>
  <div class="main-window">
      <div id="chat-window">
          <div id="messages-panel">
            <el-scrollbar max-height="500px">
                <MessageLayout v-for="message in allMessages" :key="message.id" :message="message.content" :msg-class="message.class" />
            </el-scrollbar>
          </div>
      </div>
      <div id="meassage-input">
        <el-row>
          <el-col :span="20">
            <el-input
              placeholder="Votre message..."
              v-model="input"
              v-on:keyup.enter="sendMessage()"
              clearable>
            </el-input>
          </el-col>
          <el-col :span="2">
            <el-button id="send-btn" icon="el-icon-position" type="primary" @click="sendMessage()" circle></el-button>
          </el-col>
        </el-row>
      </div>
  </div>
</template>

<script>
import MessageLayout from '@/components/MessageLayout'

export default {
  components: {
    MessageLayout,
  },
  data () {
    return {
      input: null,
      allMessages: []
    }
  },
  methods: {
    sendMessage () {
      this.messages.push({content:this.input, class:'user-message', id:this.allMessages.length})
      this.input = null
    }
  },
  computed: {
    messages () {
      return this.allMessages
    }
  }
}
</script>

<style>
#send-btn {
    margin-left: 15px;
}

#messages-panel {
    height: 500px;
    width: 600px;
    background-color: white;
    margin: auto;
}

.user-message {
    border: black 2px solid;
    background-color: chartreuse;
}
</style>