<template>
    <div>
        <v-card
    class="mx-auto"
    outlined
        >
            <v-list-item three-line>
      <v-list-item-content>
        <v-list-item-title class="float-left text-h5 mb-1">
          Address
        </v-list-item-title>
              <v-list-item>
                  <v-list-item-title> <strong>Address:</strong> </v-list-item-title>
                  <v-list-item-subtitle>
                      {{ this.$route.params.address }}
                  </v-list-item-subtitle>
              </v-list-item>
          <v-divider class="mx-4"></v-divider>
              <v-list-item>
                  <v-list-item-title> <strong>BALANCE:</strong> </v-list-item-title>
                  <v-list-item-subtitle>
                      {{ this.$route.params.balance }} {{this.$route.params.currency}}
                  </v-list-item-subtitle>
              </v-list-item>
          <v-divider class="mx-4"></v-divider>
              <v-list-item v-if="this.$route.params.btc_like">
                  <v-list-item-title> <strong>TOTAL RECEIVED:</strong> </v-list-item-title>
                  <v-list-item-subtitle>
                      {{ this.$route.params.total_received}} {{this.$route.params.currency}}
                  </v-list-item-subtitle>
              </v-list-item>
          <v-divider class="mx-4"></v-divider>
              <v-list-item v-if="this.$route.params.btc_like">
                  <v-list-item-title> <strong>TOTAL SENT:</strong> </v-list-item-title>
                  <v-list-item-subtitle>
                      {{ this.$route.params.total_sent }} {{this.$route.params.currency}}
                  </v-list-item-subtitle>
              </v-list-item>
          <v-divider class="mx-4"></v-divider>
              <v-list-item>
                  <v-list-item-title> <strong>TRANSACTIONS:</strong> </v-list-item-title>
                  <v-list-item-subtitle>
                      {{ this.$route.params.txs }}
                  </v-list-item-subtitle>
              </v-list-item>
      </v-list-item-content>

    </v-list-item>
        </v-card>
        <Transactions :trans-data="this.transactions_data" :address="this.$route.params.address" :btc_like="this.$route.params.btc_like" :divider="this.$route.params.divider" :currency="this.$route.params.currency" v-if="transactions_data"></Transactions>
        <v-progress-circular
                v-else
          indeterminate
          color="primary"
        ></v-progress-circular>
    </div>
</template>

<script>
import Transactions from "./Transactions";
import axios from 'axios';
export default {
    components: {
      Transactions
    },
    data() {
        return {
            axios: axios,
            transactions_data: null,
        }
    },
    methods: {
        init(data){
            this.transactions_data = data;
        }
    },

    created(){
        let url = 'http://127.0.0.1:8001/transactions_info';
        this.axios.post(url, JSON.parse(this.$route.params.req)).then(response => (this.init(response.data)))
    }
}
</script>

<style>
.row {
  display: flex;
}

/* Create two equal columns that sits next to each other */
.column {
  flex: 50%;
  padding: 10px;
  height: auto;
}
</style>