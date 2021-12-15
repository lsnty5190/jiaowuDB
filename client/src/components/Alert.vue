<!--
 * @Author: your name
 * @Date: 2021-12-14 14:19:03
 * @LastEditTime: 2021-12-14 14:25:34
 * @LastEditors: your name
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: \vues\flask-vue-crud\client\src\components\Alert.vue
-->
<template>
  <div>
    <b-alert variant="success" show>{{ message }}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message']
}
</script>
