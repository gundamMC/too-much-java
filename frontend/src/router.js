import VueRouter from 'vue-router';

import index from './pages/index';
import testPage from './pages/test_page';
import coursePage from './pages/course';
import unitPage from './pages/unit';
import assignmentPage from './pages/assignment';
import loginPage from './pages/login';
import Vue from "vue";

Vue.use(VueRouter);

const router = new VueRouter({
    mode: 'history',
    routes: [
        {path: '/', name: 'index', component: index},
        {path: '/test', name: 'test', component: testPage},
        {path: '/course/:id', name: 'course', component: coursePage},
        {path: '/course/:id/unit/:unit_id', name: 'unit', component: unitPage},
        {path: '/course/:id/unit/:unit_id/assignment/:assignment_id', name: 'assignment', component: assignmentPage},
        {path: '/login', name: 'login', component: loginPage}
    ]
});

export default router;