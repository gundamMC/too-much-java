import Vue from 'vue'
import App from './App.vue'
import 'element-ui/lib/theme-chalk/index.css';
import ElementUI from 'element-ui';
import locale from 'element-ui/lib/locale/lang/en'

import VueCookies from 'vue-cookies'

Vue.use(VueCookies)

// Vue.config.productionTip = false

Vue.use(ElementUI, { locale });

new Vue({
  render: h => h(App),
}).$mount('#app')
