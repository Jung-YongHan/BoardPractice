import { createRouter, createWebHistory } from 'vue-router'
import PageHome from '@/views/PageHome.vue'
import PageDetail from '@/views/PageDetail.vue'
import QuestionCreate from '@/views/QuestionCreate.vue'
import MemberLoginVue from '@/views/MemberLogin.vue'
const routes = [
  {
    path: '/',
    name: 'PageHome',
    component: PageHome
  },
  {
    path: '/detail/:index',
    name: 'PageDetail',
    component: PageDetail,
    props: true
  },
  {
    path: '/question-create',
    name: 'QuestionCreate',
    component: QuestionCreate
  },
  {
    path : '/login',
    name : 'memberLogin',
    component : MemberLoginVue
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
