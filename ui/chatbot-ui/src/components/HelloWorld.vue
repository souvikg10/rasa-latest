<template>
<div>
  <h2>CHATBOT</h2>
  <div class="chatbot">
    <p>{{msg}}</p>
    <div>
      <input type="text">
      <button>Send</button>
    </div>
    

  </div>
</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>
<style>
.chatbot{
  border: 5em;
  border-width: 3cm;
}
</style>

