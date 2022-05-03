<template>
  <div>
    <v-card
    class="mx-auto"
    outlined
        >
            <v-toolbar-title class="text-h6 pl-0">
              Latest transactions
            </v-toolbar-title>

            <div class="category-container" v-for="value in transData" :key="value">
            <Transaction :data="value" :address="address" :btc_like="btc_like" :divider="divider" :currency="currency"/>
          </div>
    </v-card>
  </div>
</template>

<script>
  import Transaction from './Transaction'
  export default {
    components: {
      Transaction
    },
    props: {
      address: String,
      transData: Array,
      btc_like: Boolean,
      divider: Number,
      currency: String
    }
  }
</script>

<style>
  .category-container {
    /*display: flex;*/
    flex-wrap: wrap;
    justify-content: space-around;
}
</style>