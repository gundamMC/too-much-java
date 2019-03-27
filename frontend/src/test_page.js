import Vue from 'vue'
import test_page from './test_page.vue'
import 'element-ui/lib/theme-chalk/index.css';
import ElementUI from 'element-ui';
import locale from 'element-ui/lib/locale/lang/en'

// Vue.config.productionTip = false

Vue.use(ElementUI, { locale });

new Vue({
  render: h => h(test_page),
}).$mount('#test_page');
