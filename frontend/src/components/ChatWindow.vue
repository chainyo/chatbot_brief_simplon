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
import * as tf from '@tensorflow/tfjs';

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
    let that = this;

    async function loadModel() {
      that.model = await tf.loadLayersModel('@/model.json');
      that.modelReady = true;
      that.predictedValue = 'Ready for making predictions';
    }
    loadModel();
  },
  methods: {
    sendMessageUser () {
      this.allMessages.push({content:this.input, class:'user-message', id:this.allMessages.length})
      this.input = null
    },
    sendMessageBot (answer) {
      this.allMessages.push({content:answer, class:'bot-message', id:this.allMessages.length})
    },
    predict() {
      this.predictedTag = this.predictValue([this.input]);
      console.log(this.predictedValue);
    },
    predictValue(input) {
      const tfarray = tf.tensor2d(input, [1, input.length]); // preprocessing
      const prediction = this.model.predict(tfarray); // prediction
      return prediction.get(0, 0); // renvoi pred
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