<template>
  <div class="main-window">
      <div id="chat-window">
          <div id="messages-panel">
            <el-scrollbar max-height="500px">
                <MessageLayout 
                  v-for="message in allMessages" 
                  :key="message.item_id" 
                  :message="message.item_content" 
                  :msgClass="message.item_class" />
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
import * as tf from '@tensorflow/tfjs'
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
      lastItemId: null
    }
  },
  mounted () {
    let that = this;
    async function loadModel() {
      that.model = await tf.loadLayersModel('http://localhost:8081/api/v1/model');
      console.log("Model loaded")
    }
    loadModel();
  },
  methods: {
    sendMessageUser () {
      this.lastItemId = this.allMessages.length
      this.allMessages.push({item_content:this.input, item_class:'user-message', item_id:this.lastItemId})
      this.input = null
      this.predictValue(this.allMessages.find(x => x.item_id === this.lastItemId))
    },
    sendMessageBot (answer) {
      this.allMessages.push({item_content:answer, item_class:'bot-message', item_id:this.allMessages.length})
    },
    predictValue(input) {
      axios
        .post('http://localhost:8081/api/v1/stemming', {
          item_content: input.item_content,
          item_class: input.item_class,
          item_id: input.item_id
        })
        .then(function(response) {
          this.model.predict(tf.tensor(response.data.data));
        })
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

#app {

  position: fixed;
  bottom: 0;
  right: 0;
  margin-bottom: 0.5em;
  margin-right: 1em;
  background-color: #fefefece;
  border-radius: 15px 15px;
  padding-top: 1em;

}

#messages-panel {
    height: 30em;
    background-color: #fffffff4;
    margin: auto;
    border-radius: 15px 15px;
    border:1px solid #bdbdbd;
}

#chat-window {
    margin-top:1.5em;
    margin-bottom:0.5em;
}

#send-btn {
    margin-left: 2em;
}

.el-card.user-message {
    text-align: right;
    background-color: rgba(251,0,51,0.1);
    float: right;
    margin-right: 10px;
    margin-top: 10px;
    border-radius: 15px 15px;
    font-family: "Alef", Arial;
    font-size: 0.9em;
    
}

.el-card.bot-message {
    text-align: left;
    background-color: rgba(251,0,51,0.5);
    float: left;
    margin-left: 10px;
    margin-top: 10px;
    border-radius: 15px 15px;
    font-family: "Alef", Arial;
    font-size: 0.9em;
}
</style>