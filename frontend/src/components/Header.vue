<template>
  <el-row id="header-col">
    <el-col :span="1" id="logo-simplon">
      <el-avatar :size="60" :src="circleUrl" :fit="fill"></el-avatar>
    </el-col>
    <el-col :span="5">
      <el-card shadow="always">Simplon</el-card>
    </el-col>
    <el-col :span="5">
      <el-card shadow="always">Github</el-card>
    </el-col>
  </el-row>
</template>

<script>
export default {
  data() {
    return {
      circleUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuMP1b3efs5mJ_dOIUitFj45a2lSUJzmIRPajONxD5CgPmgWvqhqvddsGigKjk6Gsrvzs&usqp=CAU"
    }
  }
}
</script>

<style scoped>

#header-col {
    background-color: #CE0033;
    padding: 0.5em;
    border-radius: 15px 15px;
}

#logo-simplon {
    width: 2em;
    margin-right: 3em;
    margin-left: 1em;
}

.el-card {
  margin-right: 2em ;
  min-width: 6em;
  border-radius: 5px;
  border:1px solid #353236;
  text-align: center;
  background-color: #8f888875;
  font-family: "Alef", Arial;
  font-size: 1em;
  color: #ffffff
}

.el-card:hover {
  border:1px solid #ffffffda;
  background-color: #CE0033;
  color: #ffffffc9
}

.el-col.el-col-1 {
  min-width: 4em;
  padding:0.5em;
}
.el-col.el-col-5 {
  min-width: 12em;
  padding:0.5em;
}

</style>