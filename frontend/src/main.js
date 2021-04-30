import { createApp } from 'vue'
import App from './App.vue'
import router from '@/router'

// ElementPlus components library
import ElementPlus from 'element-plus'
import 'element-plus/lib/theme-chalk/index.css'

const chatbotApp = createApp(App)
chatbotApp.use(router)
chatbotApp.use(ElementPlus)
chatbotApp.mount('#app')

