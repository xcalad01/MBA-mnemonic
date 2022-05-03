<template>
    <div>
        <v-card
        class="mx-auto"
        >
            <v-list-item three-line>
              <v-list-item-content>
                <div class="text-overline mb-4">
                    <a><strong @click="redirect(data['txid'])" style="color: dodgerblue">{{data["txid"]}}</strong></a>
                </div>
              </v-list-item-content>
            </v-list-item>

            <div style="display: flow-root" class="row">
                <div class="column"><h3>Fee:</h3> {{data["fees"] / divider}} {{currency}}</div>
                 <div class="column"><h3>Confirmations:</h3> {{data["confirmations"]}}</div>
                     <div v-if="btc_like">
                         <div class="column">
                     <h3>Value in:</h3> {{data["total_in"] / divider}} {{currency}}
                 </div>
                 <div class="column">
                     <h3>Value out:</h3> {{data["total_out"] / divider}} {{currency}}
                 </div>
                     </div>
            </div>

            <div class="row">
                <div style="display: block ruby" class="column">
                        <v-list-item three-line>
                            <v-list-item-content>
                                <div v-for="value in data['vin']" :key="value">
                                    <v-list-item>
                                        <v-list-item-title v-if="value['addresses'][0] == address"> {{value['addresses'][0]}} </v-list-item-title>
                                        <v-list-item-title v-else @click="redirect_home(value['addresses'][0])" style="color: dodgerblue"><a>{{value['addresses'][0]}}</a></v-list-item-title>
                                        <v-list-item-subtitle v-if="btc_like" style="display: contents"> {{value["value"] / divider}} {{currency}} </v-list-item-subtitle>
                                    </v-list-item>
                                </div>
                            </v-list-item-content>
                        </v-list-item>
                </div>

                <div class="column">
                    <v-avatar style="display: contents" size="20">
                      <img
                        alt="user"
                        src="../assets/green_arrow.png"
                      >
                    </v-avatar>
                </div>

                 <div style="display: block ruby" class="column">
                    <v-list-item three-line>
                            <v-list-item-content>
                                <div v-for="value in data['vout']" :key="value">
                                    <v-list-item>
                                        <v-list-item-title v-if="value['addresses'][0] == address"> {{value['addresses'][0]}} </v-list-item-title>
                                        <v-list-item-title v-else @click="redirect_home(value['addresses'][0])" style="color: dodgerblue"><a>{{value['addresses'][0]}}</a></v-list-item-title>
                                        <v-list-item-subtitle style="display: contents"> {{value["value"] / divider}} {{currency}} </v-list-item-subtitle>
                                    </v-list-item>
                                </div>
                            </v-list-item-content>
                        </v-list-item>
                </div>
            </div>
        </v-card>
    </div>


</template>

<script>
export default {
    props: {
        data: Array,
        address: String,
        btc_like: Boolean,
        divider: Number,
        currency: String,
    },
    methods : {
        redirect(txid){
            let request_data = {
                "transaction": txid,
                "token": this.currency
            };

            console.log(this.data);
            this.$router.push({ name: 'TransactionSpecific', params: {
                    req: JSON.stringify(request_data),
                    btc_like: this.btc_like,
                    token: this.currency,
                    divider: this.divider,
                    blockHeight: this.data["blockHeight"]
                }})
        },

        redirect_home(address) {
            this.$router.push({ name: 'Home', params: {
                    address: address,
                }})
        }
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