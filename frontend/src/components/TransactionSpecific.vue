<template>
    <div>
        <div v-if="btc_like">
         <v-card
        class="mx-auto"
        >
            <v-list-item three-line>
              <v-list-item-content>
                <v-toolbar-title class="text-h6 black--text pl-0">
                  DETAILS
                </v-toolbar-title>
                  <v-list-item>
                       <v-list-item-title> Transaction: </v-list-item-title>
                      <v-list-item-subtitle> {{this.transaction}}</v-list-item-subtitle>
                  </v-list-item>
                  <v-list-item>
                      <v-list-item-title> Status: </v-list-item-title>
                      <v-list-item-subtitle style="color: #9C1A1C" v-if=" !('confirmations' in tx_data) || tx_data['confirmations'] == 0">
                          <strong>Not confirmed</strong>
                      </v-list-item-subtitle>
                      <v-list-item-subtitle v-else style="color: #3A7734">
                          <strong>Confirmed</strong>
                      </v-list-item-subtitle>
                  </v-list-item>

                  <v-list-item>
                       <v-list-item-title> Received Time: </v-list-item-title>
                      <v-list-item-subtitle v-if="'time' in tx_data"> {{new Date(tx_data["time"] * 1000)}}</v-list-item-subtitle>
                      <v-list-item-subtitle v-else></v-list-item-subtitle>

                  </v-list-item>

                  <v-list-item>
                       <v-list-item-title> Size: </v-list-item-title>
                      <v-list-item-subtitle> {{tx_data["size"]}}</v-list-item-subtitle>
                  </v-list-item>

                  <v-list-item>
                       <v-list-item-title> Weight: </v-list-item-title>
                      <v-list-item-subtitle> {{tx_data["weight"]}}</v-list-item-subtitle>
                  </v-list-item>

                   <v-list-item>
                       <v-list-item-title> Confirmations: </v-list-item-title>
                      <v-list-item-subtitle> {{tx_data['confirmations']}}</v-list-item-subtitle>
                  </v-list-item>

                  <v-list-item>
                       <v-list-item-title> Inccluded in Block: </v-list-item-title>
                      <v-list-item-subtitle> <a href='blockUrl'> {{this.$route.params.blockHeight}} </a> </v-list-item-subtitle>
                  </v-list-item>

              </v-list-item-content>
            </v-list-item>
         </v-card>

         <v-card
        class="mx-auto"
        >
             <v-list-item three-line>
              <v-list-item-content>
                <v-toolbar-title class="text-h6 black--text pl-0">
                  INPUTS
                </v-toolbar-title>
                <div v-for="(value, index) in tx_data['vin']" :key="value">
                    <v-list-item>
                       <v-list-item-title> Index: </v-list-item-title>
                       <v-list-item-subtitle> {{index}}</v-list-item-subtitle>
                    </v-list-item>

                    <v-list-item>
                       <v-list-item-title> SigScript: </v-list-item-title>
                       <v-list-item-subtitle> {{value["scriptSig"]["asm"]}}</v-list-item-subtitle>
                    </v-list-item>

                    <v-list-item>
                       <v-list-item-title v-if="value['txinwitness']"> Witnesses: </v-list-item-title>
                        <v-list-item-subtitle>
                            <div v-for="value1 in value['txinwitness']" :key="value1">
                              <v-list-item>
                                    <v-list-item-subtitle> {{value1}}</v-list-item-subtitle>
                               </v-list-item>
                        </div>
                        </v-list-item-subtitle>
                  </v-list-item>
                  <v-divider class="mx-4"></v-divider>
                </div>
              </v-list-item-content>
             </v-list-item>

         </v-card>

        <v-card
        class="mx-auto"
        >
             <v-list-item three-line>
              <v-list-item-content>
                <v-toolbar-title class="text-h6 black--text pl-0">
                  OUTPUTS
                </v-toolbar-title>
                <div v-for="(value, index) in tx_data['vout']" :key="value">
                    <v-list-item>
                       <v-list-item-title> Index: </v-list-item-title>
                       <v-list-item-subtitle> {{index}}</v-list-item-subtitle>
                    </v-list-item>

                    <v-list-item>
                       <v-list-item-title> Address: </v-list-item-title>
                        <v-list-item-subtitle v-if="token=='BTC'" @click="redirect_home(value['scriptPubKey']['address'])" style="color: dodgerblue"> <a>{{value["scriptPubKey"]["address"]}} </a> </v-list-item-subtitle>
                        <v-list-item-subtitle v-else @click="redirect_home(value['scriptPubKey']['addresses'][0])" style="color: dodgerblue"> <a>{{value["scriptPubKey"]["addresses"][0]}} </a> </v-list-item-subtitle>
                    </v-list-item>

                    <v-list-item>
                       <v-list-item-title> PubKeyScript: </v-list-item-title>
                       <v-list-item-subtitle> {{value["scriptPubKey"]["asm"]}}</v-list-item-subtitle>
                    </v-list-item>
                    <v-divider class="mx-4"></v-divider>
                </div>
              </v-list-item-content>
             </v-list-item>

         </v-card>
    </div>

    <div v-else>
         <v-card
        class="mx-auto"
        >
            <v-list-item three-line>
              <v-list-item-content>
                <v-toolbar-title class="text-h6 black--text pl-0">
                  DETAILS
                </v-toolbar-title>
                  <v-list-item>
                       <v-list-item-title> Transaction: </v-list-item-title>
                      <v-list-item-subtitle> {{this.transaction}}</v-list-item-subtitle>
                  </v-list-item>
                  <v-list-item>
                       <v-list-item-title> From: </v-list-item-title>
                      <v-list-item-subtitle @click="redirect_home(tx_data['tx']['from'])" style="color: dodgerblue"> <a>{{tx_data["tx"]["from"]}}</a> </v-list-item-subtitle>
                  </v-list-item>

                  <v-list-item>
                       <v-list-item-title> To: </v-list-item-title>
                      <v-list-item-subtitle @click="redirect_home(tx_data['tx']['to'])" style="color: dodgerblue"> <a>{{tx_data["tx"]["to"]}}</a> </v-list-item-subtitle>
                  </v-list-item>

                   <v-list-item>
                       <v-list-item-title> Amount: </v-list-item-title>
                      <v-list-item-subtitle> {{ parseInt(tx_data["tx"]['value'], 16) / this.$route.params.divider}} ETH</v-list-item-subtitle>
                  </v-list-item>

                   <v-list-item>
                       <v-list-item-title> Nonce: </v-list-item-title>
                      <v-list-item-subtitle> {{ parseInt(tx_data["tx"]['nonce'], 16) }}</v-list-item-subtitle>
                  </v-list-item>

                    <v-list-item>
                       <v-list-item-title> Gas Price: </v-list-item-title>
                      <v-list-item-subtitle> {{ parseInt(tx_data["tx"]['gasPrice'], 16) / this.$route.params.divider}} ETH</v-list-item-subtitle>
                  </v-list-item>

                  <v-list-item>
                       <v-list-item-title> Gas Used: </v-list-item-title>
                      <v-list-item-subtitle> {{ parseInt(tx_data['receipt']['gasUsed'], 16)}}</v-list-item-subtitle>
                  </v-list-item>
              </v-list-item-content>
            </v-list-item>
         </v-card>
    </div>
    </div>
</template>

<script>
    import axios from 'axios';
export default {
    name: "TransactionSpecific",
    data () {
        return  {
            tx_data: {},
            axios: axios,
            btc_like: null,
            transaction: null,
            token: null
        }
    },
    methods: {
        init(data){
            this.tx_data = data
        },
        redirect_home(address) {
            this.$router.push({ name: 'Home', params: {
                    address: address
                }})
        }
    },

    created() {
        this.blockUrl = "https://www.blockchain.com/btc/block/" + this.$route.params.blockHeight;
        this.btc_like = this.$route.params.btc_like;
        this.token = this.$route.params.token;
        this.transaction =  JSON.parse(this.$route.params.req)["transaction"];
        let url = 'http://localhost:8001/transaction_specific';
        this.axios.post(url, JSON.parse(this.$route.params.req)).then(response => (this.init(response.data)))
    }
}
</script>

<style>

</style>