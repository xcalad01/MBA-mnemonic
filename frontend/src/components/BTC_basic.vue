<template>
    <div>
        <v-card
    class="mx-auto"
    elevation="11"
    shaped
  >
            <v-avatar size="56">
              <img
                alt="user"
                src="../assets/bitcoin-btc-logo.png"
              >
            </v-avatar>
    <v-list-item three-line>
      <v-list-item-content>
        <v-list-item-title class="text-h5 mb-1">
          Bitcoin
        </v-list-item-title>
          <div v-if="this.requested">
              <div v-if="balance != null">
                  <v-list-item>
                      <v-list-item-title> BALANCE: </v-list-item-title>
                      <v-list-item-subtitle class="text-right">
                          {{ balance }} BTC
                      </v-list-item-subtitle>
                  </v-list-item>
                  <v-list-item>
                      <v-list-item-title> TOTAL RECEIVED: </v-list-item-title>
                      <v-list-item-subtitle class="text-right">
                          {{ total_received }} BTC
                      </v-list-item-subtitle>
                  </v-list-item>
                  <v-list-item>
                      <v-list-item-title> TOTAL SENT: </v-list-item-title>
                      <v-list-item-subtitle class="text-right">
                          {{ total_sent}} BTC
                      </v-list-item-subtitle>
                  </v-list-item>
                  <v-list-item>
                      <v-list-item-title> TRANSACTIONS: </v-list-item-title>
                      <v-list-item-subtitle class="text-right">
                          {{ txs }}
                      </v-list-item-subtitle>
                  </v-list-item>
                  <v-list-item>
                      <v-list-item-title> UNCONFIRMED TRANSACTIONS: </v-list-item-title>
                      <v-list-item-subtitle class="text-right">
                          {{ unc_txs }}
                      </v-list-item-subtitle>
                  </v-list-item>
              </div>
              <div v-else>
                  Address does not exists
              </div>
          </div>
          <div v-else-if="this.current_requesting">
              <v-progress-circular
                  indeterminate
                  color="primary"
                ></v-progress-circular>
          </div>
      </v-list-item-content>

    </v-list-item>

    <v-card-actions v-if="txs > 0">
      <v-btn
      rounded
      color="primary"
      dark
      @click="redirect()"
    >
      Transactions Info
    </v-btn>
    </v-card-actions>
  </v-card>
    </div>
</template>


<script>
    import axios from 'axios';

export default {
    name: 'BtcBasic',
    data(){
        return {
            axios: axios,
            balance: null,
            total_received: null,
            total_sent: null,
            txs: null,
            unc_txs: null,
            address_specific_req: {},
            address: null,
            requested: null,
            current_requesting: null
        }
    },
    methods: {
        init(data){
            this.current_requesting = false;
            this.requested = true;
            if (data["balance"]) {
                this.balance = data["balance"] / 100000000;
                this.total_received = data["totalReceived"] / 100000000;
                this.total_sent = data["totalSent"] / 100000000;
                this.txs = data["txs"];
                this.unc_txs = data["unconfirmedTxs"];

                this.address_specific_req = {
                    "transactions": data["txids"],
                    "token": "BTC",
                    "first_n": 10,
                };
            } else {
                this.balance = null;
                this.total_received = null;
                this.total_sent = null;
                this.txs = null;
                this.unc_txs = null;
            }
        },
        request_addr_info(address){
            this.current_requesting = true;
            this.requested = false;
            this.address = address;
            let url = 'http://127.0.0.1:8001/check_address?token=BTC&address=' + address;
            this.axios.get(url).then(response => (this.init(response.data)));
        },
        redirect() {
            this.$router.push({ name: 'AddressSpecific', params: {
                req: JSON.stringify(this.address_specific_req),
                balance: this.balance,
                total_received: this.total_received,
                total_sent: this.total_sent,
                txs: this.txs,
                address: this.address,
                btc_like: true,
                currency: "BTC",
                divider: 100000000
            }})
        }
    }
}

</script>

<style>
    .flex {
    display: flex;
}
    .img {
        height: 24%;
        width: 12%;
    }
</style>