<template>
  <div class="dashboard-container">
    <p><div class="dashboard-text" align='center'>Welcome To JiaoWUDB!</div>
    <p class='big'><div class="front-text" align="center">Contributers: 傅云濠 赵浩然 梁笑钰 李绍宁</div>
    <img src="@/assets/front/ER.jpg" alt="error">
  </div>
</template>



<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name'
    ])
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 50px;
  }
  &-text {
    font-size: 60px;
    line-height: 46px;
  }
}
</style>

<style lang="scss" scoped>
.front {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
