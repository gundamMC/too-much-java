import Vue from 'vue';
import Vuex from 'vuex';
import auth from './modules/auth';
import course from './modules/course';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    course
  },
})