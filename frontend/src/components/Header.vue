<template>
  <el-row id="header-col">
    <el-col :span="1" id="logo-simplon">
      <el-avatar :size="50" :src="circleUrl"></el-avatar>
    </el-col>
    <el-col :span="5">
      <el-card shadow="hover">Simplon</el-card>
    </el-col>
    <el-col :span="5">
      <el-card shadow="hover">Github</el-card>
    </el-col>
  </el-row>
</template>

<script>
export default {

}
</script>

<style scoped>
#header-col {
    background-color: #CE0033;
    height: 120%;
}

</style>