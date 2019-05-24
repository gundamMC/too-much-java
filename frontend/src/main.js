import Vue from 'vue/dist/vue.js';
import VueRouter from 'vue-router'
import App from './App.vue'
import index from './pages/index'
import testPage from './pages/test_page.vue'
import 'element-ui/lib/theme-chalk/index.css';
import ElementUI from 'element-ui';
import locale from 'element-ui/lib/locale/lang/en'

import VueCookies from 'vue-cookies'

Vue.use(VueRouter);
Vue.use(VueCookies);

const router = new VueRouter({
  mode: 'history',
  routes: [
    {path: '/', name: 'index', component: index},
    {path: '/test', name: 'test', component: testPage}
  ] 
});

// Vue.config.productionTip = false

Vue.use(ElementUI, { locale });

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
