<template>
  <div>
    <ul v-if="items && items.length">
    <li v-for="item in items" :key="item.id">
      <p><strong>{{item.name}}</strong></p>
      <p>{{item.description}}</p>
    </li>
  </ul>
  <ul v-if="errors && errors.length">
    <li v-for="error in errors" :key="error.id">
      {{error.message}}
    </li>
  </ul>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'items',
  data () {
    return {
      items: [],
      errors: []
    }
  },
  mounted () {
    axios({
      method: 'get',
      url: `http://localhost:8000/api/items/`,
      auth: {
        username: 'kapil',
        password: 'Sanju1992$'
      }
    })
      .then(response => {
        this.items = response.data
      })
      .catch(e => {
        this.errors.push(e)
        console.log(e)
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
