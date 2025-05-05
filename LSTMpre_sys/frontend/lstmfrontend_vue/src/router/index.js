import { createRouter, createWebHashHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import SearchView from '@/views/SearchView.vue';
import PredictView from '@/views/PredictView.vue';
import HelpView from '@/views/HelpView.vue';

const routes = [
  { path: '/',
    name: 'home',
    component: HomeView,
    meta: { title: 'Home' }
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView,
    meta: { title: 'Search' }
  },
  {
    path: '/predict',
    name: 'predict',
    component: PredictView,
    meta: { title: 'Predict' }
  },
  {
    path: '/help',
    name: 'help',
    component: HelpView,
    meta: { title: 'Help' }
  },
  {
    path: '/login',
    name: 'Login', // 添加路由名称
    component: () => import('@/views/login/index.vue')
  },
  {
    path: '/dashboard',
    component: () => import('@/views/HomeView.vue'),
    children: [
      { path: '', redirect: 'search' }, // 默认重定向到搜索页
      { path: 'search', component: () => import('@/views/SearchView.vue') },
      { path: 'predict', component: () => import('@/views/PredictView.vue') },
      { path: 'help', component: () => import('@/views/HelpView.vue') }
    ]
  },
  // 添加一个通配符路由来处理未匹配的路由
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
];

const router = createRouter({
    history: createWebHashHistory(),
    routes
    });



export default router

/*

import Login from '@/views/login/index.vue';
import Home from '@/views/index.vue';
import Layout from '@/layout/index.vue';
import { pa } from 'element-plus/es/locale/index.mjs';



静态路由配置
const routes = [
    {
        path: '/',
        redirect: '/login'
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('@/views/login/index.vue'),
        hidden: true
    },
    {
        path:'/404',
        component: () => import('@/views/404.vue'),
        hidden: true
    },
    {
        path:'/',
        component: Layout,
        redirect: '/dashboard',
        children:[
            {
                path: 'dashboard',
                name: 'Dashboard',
                component: () => import('@/views/dashboard/index.vue'),
                meta: { title: 'Dashboard', icon: 'dashboard' }
            }
        ]
    },
    {
        path: '/',  //路径
        name: 'Home',  //名字
        component: () => import('@/views/index.vue')  //
    }
]


const router = createRouter({
    history: createWebHashHistory(),
    routes:constantRoutes,
    scrollBehavior: () => ({ top: 0 })
})

//动态加载菜单路由
import { fetchMenuList } from '@/api/menu.js'

fetchMenuList().then(response => {
    const manuData = response.data

    munuData.forEach(manu => {
        //生成子动态路由
        const children = manu.children.map(child => ({
            path: child.path,
            name: child.name,
            component: () => import('@/views/table/index.vue'),
            meta: { title: child.name, icon: 'table' }
        }))
        //
        const parentRoute = {
            path:'/',
            component: Layout,
            name: manu.name.replace(/\s+/g, '-'),
            redirect:{name:manu.children[0]?.name}, //重定向到第一个子路由
            mata: { title: manu.name, icon: 'el-icon-s-help' },
            children
        }
        router.addRoute(parentRoute)
    })
    //添加404页面
    router.addRoute({ 
        path: '/:pathMatch(.*)*', 
        redirect: '/404', 
        hidden: true 
    })
})

//重置路由办法vue3
export function resetRouter() {
    //移除所有动态添加的路由
    router.getRoutes().forEach(route => {
        if (route.name && !constantRoutes.find(r => r.name === route.name)) {
            router.removeRoute(route.name)
        }
    })
    //重新添加基础路由
    constantRoutes.forEach(route => {
        if (!router.hasRoute(route.name)) {
            router.addRoute(route)
        }
    })
}*/

