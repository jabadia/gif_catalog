import Vue from 'vue';
import Router from 'vue-router';
import GifHome from './components/GifHome.vue';
import GifDetail from './components/GifDetail.vue';
import Error404 from './components/Error404.vue';

Vue.use(Router);

const router = new Router({
    mode: 'history',
    routes: [
        {path: '/', name: 'home', component: GifHome},
        {path: '/detail/:id', name: 'detail', component: GifDetail, props:true},
        {path: '*', component: Error404}, // Not found
    ],
});

router.beforeEach((to, from, next) => {
    console.log('routing from', from.path, 'to', to.path);
    next();
});

export default router;
