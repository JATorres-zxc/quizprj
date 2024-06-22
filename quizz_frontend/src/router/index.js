import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '@/views/SignupView.vue'
import LoginView from '@/views/LoginView.vue'
import EnterCodeView from '@/views/EnterCodeView.vue'
import QuizInitializationView from '@/views/QuizInitializationView.vue'
import QuizView from '@/views/QuizView.vue'
import FlipCard from '@/views/FlipCard.vue'
import CreateCard from '@/views/CreateCard.vue'
import CreateQuiz from '@/views/CreateQuiz.vue'







const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/entercode',
      name: 'entercode',
      component: EnterCodeView
    },
    {
      path: '/quizInitialization',
      name: 'quizInitialization',
      component: QuizInitializationView
    },
    {
      path: '/quiz',
      name: 'quiz',
      component: QuizView
    },
    {
      path: '/flipcard',
      name: 'flipcard',
      component: FlipCard
    },
    {
      path: '/createcard',
      name: 'createcard',
      component: CreateCard
    },
    {
      path: '/createquiz',
      name: 'createquiz',
      component: CreateQuiz
    },
  ]
})

export default router
