import Vue from 'vue/dist/vue.js';
import VueRouter from 'vue-router'
import 'element-ui/lib/theme-chalk/index.css';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/reset.css';
import locale from 'element-ui/lib/locale/lang/en';

import VueCookies from 'vue-cookies';

import App from './App.vue';
import index from './pages/index';
import testPage from './pages/test_page';
import coursePage from './pages/course';
import unitPage from './pages/unit';
import assignmentPage from './pages/assignment';

Vue.use(VueRouter);
Vue.use(VueCookies);

const router = new VueRouter({
  mode: 'history',
  routes: [
    {path: '/', name: 'index', component: index},
    {path: '/test', name: 'test', component: testPage},
    {path: '/course/:id', name: 'course', component: coursePage},
    {path: '/course/:id/unit/:unit_id', name: 'unit', component: unitPage},
    {path: '/course/:id/unit/:unit_id/assignment/:assignment_id', name: 'assignment', component: assignmentPage}
  ] 
});

// Vue.config.productionTip = false

Vue.use(ElementUI, { locale });

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
