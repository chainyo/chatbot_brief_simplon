<template>
  <p v-bind:class="[msgClass]">{{ message }}</p>
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