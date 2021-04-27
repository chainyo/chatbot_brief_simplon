import { createRouter, createWebHistory } from 'vue-router'
import ChatBot from '@/pages/ChatBot.vue'

const routes = [
  {
    path: '/',
    name: 'ChatBot',
    component: ChatBot
  }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
