<template>
  <div>
           <h4>Address</h4>
           <v-text-field
            label="Address"
            placeholder="Fill address"
            filled
            rounded
            dense
            v-model="address"
          ></v-text-field>

          <v-btn
      class="ma-2"
      outlined
      color="indigo"
      @click="update()"
    >
      Check Address
    </v-btn>

      <div class="row">
          <BtcBasic class="column" ref="btcbasic"></BtcBasic>
          <BCHBasic class="column" ref="bchbasic"></BCHBasic>
          <BTGBasic class="column" ref="btgbasic"></BTGBasic>
      </div>
      <div class="row2">
          <EthBasic class="column" ref="ethbasic"></EthBasic>
          <DogeBasic class="column" ref="dogebasic"></DogeBasic>
      </div>
  </div>
</template>

<script>
import BtcBasic from '../components/BTC_basic.vue'
import EthBasic from '../components/ETH_basic.vue'
import DogeBasic from '../components/DOGE_basic.vue'
import BCHBasic from '../components/BCH_basic.vue'
import BTGBasic from '../components/BTG_basic.vue'

export default {
    name: 'Home',
    components: {
      BtcBasic,
      EthBasic,
      DogeBasic,
      BCHBasic,
      BTGBasic
    },
    data(){
      return {
        counter: 0,
        address: "",
        addr_requested: false
      }
    },
    methods: {
      update(){
        this.$refs.btcbasic.request_addr_info(this.address);
        this.$refs.ethbasic.request_addr_info(this.address);
        this.$refs.dogebasic.request_addr_info(this.address);
        this.$refs.bchbasic.request_addr_info(this.address);
        this.$refs.btgbasic.request_addr_info(this.address);
      }
    },

    mounted() {
        if (this.$route.params.address) {
            this.address = this.$route.params.address;
            this.update();
        }
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.column {
  float: left;
  width: 50%;
  padding: 5px;
}

.row::after {
  content: "";
  clear: both;
  display: table;
}
  .flex {
    display: flex;
}

.button {
  padding: 10px 20px;
  border: 1px solid #ddd;
  color: #333;
  background-color:#fff;
  border-radius: 4px;
  font-size: 14px;
    display: flex;
    margin-top: 10px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: auto;
  width: 10%;
}
.center {
  display: flex;
  margin: auto;
  width: 100%;
}
    .input {
        margin-left: 10px;
    }
    .base {
        margin-left: 100px;
        margin-top: 70px;
    }
    .base2 {
        margin-top: 70px;
    }

    .row {
        padding-top: auto;
  display: flex;
}
    .row2 {
        padding-top: auto;
  display: flex;
}

/* Create two equal columns that sits next to each other */
.column {
  flex: 50%;
  padding: 10px;
    height: auto;
}
</style>

