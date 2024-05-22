import {RouteRecordRaw} from 'vue-router';
import {useAuthStore} from "stores/authStore";

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: 'articles',
        name: 'article-list',
        component: () => import('pages/ArticleList.vue'),
      }
    ],
    beforeEnter: (to,from) =>{
      const authStore = useAuthStore()
      if(!authStore.$state.isAuthenticated) {
        return {name: 'login'}
      }
    }
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('pages/LoginView.vue'),
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
