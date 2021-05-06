<template>
  <div class="main-window">
      <div id="chat-window">
          <div id="messages-panel">
            <el-scrollbar>
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
      lastItemId: null,
      tensor: [],
      allTags: {
        0:"admission1",
        1:"admission2",
        2:"contact",
        3:"credentials",
        4:"degree",
        5:"evaluation",
        6:"goodbye",
        7:"howareyou",
        8:"interviews1",
        9:"price",
        10:"program",
        11:"salutations",
        12:"school1",
        13:"school2",
        14:"thanks"}
    }
  },
  methods: {
    sendMessageUser () {
      this.lastItemId = this.allMessages.length
      if (this.input) {
        this.allMessages.push({item_content:this.input, item_class:'user-message', item_id:this.lastItemId})
        this.predictValue(this.allMessages.find(x => x.item_id === this.lastItemId))
      }
    },
    sendMessageBot (answer) {
      this.allMessages.push({item_content:answer, item_class:'bot-message', item_id:this.allMessages.length})
    },
    async predictValue(input) {
      axios
        .post('http://localhost:8081/api/v1/stemming', {
          item_content: input.item_content,
          item_class: input.item_class,
          item_id: input.item_id
        })
        .then(response => (this.tensor = response.data.data))
      this.input = null
      const model = await tf.loadLayersModel('http://localhost:8081/api/v1/model')
      let prediction = await model.predict(tf.tensor([this.tensor])).argMax(-1).data()
      this.predictedTag = await this.allTags[prediction]
      await axios
        .get(`http://localhost:8081/api/v1/find_one?tag=${this.predictedTag}`)
        .then(response => (this.botAnswer = response.data.responses[Math.floor(Math.random() * response.data.responses.length)]))
      await this.sendMessageBot(this.botAnswer)
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
    min-height: 20em;
    max-height: 28em;
    height:24em;
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
    margin-right: 1em;
    margin-top: 1em;
    border-radius: 15px 15px;
    font-family: "Alef", Arial;
    font-size: 0.9em;
    max-width: 20em;
    
}

.el-card.bot-message {
    text-align: left;
    background-color: rgba(251,0,51,0.5);
    float: left;
    margin-left: 1em;
    margin-top: 1em;
    border-radius: 15px 15px;
    font-family: "Alef", Arial;
    font-size: 0.9em;
    max-width: 20em;
}
.el-scrollbar__wrap{
  overflow-y:scroll;
}
</style>