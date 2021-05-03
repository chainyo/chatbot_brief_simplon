<template>
  <div class="main-window">
      <div id="chat-window">
          <div id="messages-panel">
            <el-scrollbar max-height="500px">
                <MessageLayout 
                  v-for="message in allMessages" 
                  :key="message.id" 
                  :message="message.content" 
                  :msgClass="message.class" />
            </el-scrollbar>
          </div>
      </div>
      <div id="meassage-input">
        <el-row>
          <el-col :span="20">
            <el-input
              placeholder="Votre message..."
              v-model="input"
              v-on:keyup.enter="sendMessageUser()"
              clearable>
            </el-input>
          </el-col>
          <el-col :span="2">
            <el-button id="send-btn" icon="el-icon-position" type="primary" @click="sendMessageUser()" circle></el-button>
          </el-col>
        </el-row>
      </div>
  </div>
</template>

<script>
import MessageLayout from '@/components/MessageLayout'
import axios from 'axios'

export default {
  components: {
    MessageLayout,
  },
  data () {
    return {
      input: null,
      allMessages: [],
      botAnswer: null,
      predictedTag: null,
    }
  },
  mounted () {
    async function loadModel() {
      const tf = require("@tensorflow/tfjs");
      const model = await tf.loadLayersModel('http://localhost:8081/api/v1/model');
      console.log("Model loaded")
      console.log(model.summary)
    }
    loadModel();
  },
  methods: {
    sendMessageUser () {
      const storedInput = this.input
      this.allMessages.push({content:this.input, class:'user-message', id:this.allMessages.length})
      this.input = null
      this.predictedTag = this.predictValue(storedInput)
      console.log(this.predictedTag)
    },
    sendMessageBot (answer) {
      this.allMessages.push({content:answer, class:'bot-message', id:this.allMessages.length})
    },
    predictValue(input) {
      const preprocessing = axios.get(`http://api:8081/api/v1/stemming?${input}`)
      const prediction = this.model.predict(preprocessing.data);
      return prediction
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

.el-card.user-message {
    text-align: right;
    background-color: rgba(251,0,51,0.1);
    float: right;
    margin-right: 10px;
    margin-top: 10px;
    border-radius: 15px 15px;
}

.el-card.bot-message {
    text-align: left;
    background-color: rgba(251,0,51,0.5);
    float: left;
    margin-left: 10px;
    margin-top: 10px;
    border-radius: 15px 15px;
}
</style>