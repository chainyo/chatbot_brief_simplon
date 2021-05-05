<template>
  <el-row class="message">
    <el-col :offset="0">
      <el-card 
        shadow="always" 
        :class="[msgClass]">
        <span>{{ message }}</span>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
export default {
  props: {
    message: {
      type: String,
      required: true
    },
    msgClass: {
      type: String,
      required: true
    }
  }
}
</script>

<style>
</style>