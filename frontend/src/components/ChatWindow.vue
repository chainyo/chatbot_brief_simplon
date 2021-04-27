<template>
  <div class="main-window">
      <div id="chat-window"></div>
      <div id="meassage-input">
        <el-row>
          <el-input
            placeholder="Votre message..."
            v-model="input"
            clearable>
          </el-input>
          <el-button icon="el-icon-position" type="primary" @click="sendMessage()" circle></el-button>
        </el-row>
      </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      input: null
    }
  },
  methods: {
    sendMessage () {

    }
  }
}
</script>

<style>

</style>