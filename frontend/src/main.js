import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

const app = createApp(App)
app.use(router).mount('#app')
window.Kakao.init("51cdee165f32192ab3145096c2da3462");