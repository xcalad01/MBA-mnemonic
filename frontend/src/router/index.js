import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import AddressSpecific from "../components/AddressSpecific";
import TransactionSpecific from "../components/TransactionSpecific"
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/address',
    name: 'AddressSpecific',
    component: AddressSpecific
  },
  {
    path: "/transaction",
    name: "TransactionSpecific",
    component: TransactionSpecific
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
