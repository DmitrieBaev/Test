<template>
  <div class="home">
      <p class="h1 mb-3">Выберите вопросник из списка:</p>
      <div v-for="currency in questionary" class="currency">
        <router-link :to="{name: 'questionary-by-id', params: {id: currency.pk}}">{{ currency.caption }}</router-link>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return { questionary: null }
  },
  mounted() {
    axios
        .get('/api/v1/questionary/')
        .then(response => (this.questionary = response.data.results))
  }
}
</script>
