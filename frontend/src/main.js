import Vue from 'vue';
import 'element-ui/lib/theme-chalk/index.css';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/reset.css';
import locale from 'element-ui/lib/locale/lang/en';

import VueCookies from 'vue-cookies';

// router
import router from './router';
// vuex store
import store from './store'

import App from './App.vue';

import axios from "axios";
import $axios from './axios-instance';

axios.defaults.headers.common['Authorization'] =
                                'jwt ' + store.getters.token;


Vue.use({
    install (Vue) {
    Vue.prototype.$api = $axios
  }
});

Vue.use(VueCookies);



// Vue.config.productionTip = false

Vue.use(ElementUI, { locale });

const vm = new Vue({
    router,
    store,
    render: h => h(App)
});

vm.$mount('#app');

export default vm;
