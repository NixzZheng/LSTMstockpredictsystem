import { createApp } from 'vue'
//import { createStore } from 'vuex'    25.3.22把vuex删了，换成pinia
import {createPinia} from 'pinia'
import { ElementPlus } from '@element-plus/icons-vue'
import Echarts from 'vue-echarts'
import {use} from 'echarts/core'
import './style.css'
import App from './App.vue'
import router from './router/index.js'
import '@/assets/css/index.css'
import '@/assets/css/common.css'
import '@/assets/css/iconfont.css'

const app = createApp(App)
app.component('v-chart', Echarts)
app.use(createPinia())
app.use(router)
app.use(ElementPlus)
app.mount('#app')
//createApp(App).mount('#app')
