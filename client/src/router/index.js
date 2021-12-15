import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: 'Dashboard', icon: 'dashboard' }
    }]
  },

  // {
  //   path: '/example',
  //   component: Layout,
  //   redirect: '/example/table',
  //   name: 'Example',
  //   meta: { title: 'Example', icon: 'el-icon-s-help' },
  //   children: [
  //     {
  //       path: 'table',
  //       name: 'Table',
  //       component: () => import('@/views/table/index'),
  //       meta: { title: 'Table', icon: 'table' }
  //     },
  //     {
  //       path: 'tree',
  //       name: 'Tree',
  //       component: () => import('@/views/tree/index'),
  //       meta: { title: 'Tree', icon: 'tree' }
  //     }
  //   ]
  // },

  // {
  //   path: '/form',
  //   component: Layout,
  //   children: [
  //     {
  //       path: 'index',
  //       name: 'Form',
  //       component: () => import('@/views/form/index'),
  //       meta: { title: 'Form', icon: 'form' }
  //     }
  //   ]
  // },

  {
    path: '/nested',
    component: Layout,
    redirect: '/nested/menu1',
    name: 'Nested',
    meta: {
      title: 'JiaoWU',
      icon: 'nested'
    },
    children: [
      {
        path: 'menu2',
        component: () => import('@/views/nested/menu2/index'),
        name: 'Menu2',
        meta: { title: 'Course' }
      },
      {
        path: 'menu3',
        component: () => import('@/views/nested/menu3/index'),
        name: 'Menu3',
        meta: { title: 'Student' }
      },
      {
        path: 'menu4',
        component: () => import('@/views/nested/menu4/index'),
        name: 'Menu4',
        meta: { title: 'Department' }
      },
      {
        path: 'menu5',
        component: () => import('@/views/nested/menu5/index'),
        name: 'Menu5',
        meta: { title: 'Section' }
      },
      {
        path: 'menu6',
        component: () => import('@/views/nested/menu6/index'),
        name: 'Menu6',
        meta: { title: 'Takes' }
      },
      {
        path: 'menu7',
        component: () => import('@/views/nested/menu7/index'),
        name: 'Menu7',
        meta: { title: 'Teacher' }
      },
      {
        path: 'menu8',
        component: () => import('@/views/nested/menu8/index'),
        name: 'Menu8',
        meta: { title: 'Teach' }
      }
    ]
  },

  {
    path: '/function',
    component: Layout,
    // redirect: '/nested/menu1',
    name: 'Function',
    meta: {
      title: 'Function',
      icon: 'nested'
    },
    children: [
      {
        path: 'menu1',
        component: () => import('@/views/function/menu1/index'),
        name: 'Menu1',
        meta: { title: '查询课表(学生)' }
      },
      {
        path: 'menu2',
        component: () => import('@/views/function/menu2/index'),
        name: 'Menu2',
        meta: { title: '查询开课信息' }
      },
      {
        path: 'menu3',
        component: () => import('@/views/function/menu3/index'),
        name: 'Menu3',
        meta: { title: '查询教室占用' }
      },
      {
        path: 'menu4',
        component: () => import('@/views/function/menu4/index'),
        name: 'Menu4',
        meta: { title: '查询课表(老师)' }
      }
    ]
  },

  // {
  //   path: 'external-link',
  //   component: Layout,
  //   children: [
  //     {
  //       path: 'https://panjiachen.github.io/vue-element-admin-site/#/',
  //       meta: { title: 'External Link', icon: 'link' }
  //     }
  //   ]
  // },

  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
