import $axios from '../../axios-instance';
import jwt_decode from 'jwt-decode';
import router from '../../router';
import axios from "axios";
import store from "../index";

const state = {
    jwt: localStorage.getItem('token'),
    loginLoading: false,
    endpoints: {
      obtainJWT: 'auth/obtain_token/',
      refreshJWT: 'auth/refresh_token/'
    }
};

const mutations = {
    updateToken(state, newToken){
        localStorage.setItem('token', newToken);
        state.jwt = newToken;

        axios.defaults.headers.common['Authorization'] =
                                'jwt ' + store.getters.token;
    },
    removeToken(state){
        localStorage.removeItem('token');
        state.jwt = null;
    },
    startLoading(state) {
        state.loginLoading = true;
    },
    finishLoading(state) {
        state.loginLoading = false;
    }
};

const actions = {
    obtainToken(context, data) {

        context.commit('startLoading');

        let payload = {username: data.username, password: data.password};

        $axios.post(context.state.endpoints.obtainJWT, payload)
            .then((response) => {
                context.commit('updateToken', response.data.token);
                context.dispatch('getCourses');
                router.push('/');
            })
            .catch((error) => {
                if (error.response) {
                    // The request was made and the server responded with a status code
                    // that falls out of the range of 2xx

                    if (error.response.status === 400){
                        data.responseMessage(error.response.data.non_field_errors[0]);
                    }
                }
            })
            .finally(() => (context.commit('finishLoading')))
    },
    refreshToken(context) {
        const payload = {
            token: state.jwt
        };
        $axios.post(state.endpoints.refreshJWT, payload)
            .then((response) => {
                context.commit('updateToken', response.data.token);
                context.dispatch('getCourses');
            })
            .catch((error) => {
                if (error.response.status === 400){
                    // for some reason the token did not work, log out
                    context.commit('removeToken');
                }
            })
    },
    inspectToken(context) {

        return new Promise((resolve) => {
            const token = context.getters.token;
            if (token) {
                const decoded = jwt_decode(token);
                const exp = decoded.exp;
                const orig_iat = decoded.orig_iat;

                if ((Date.now()/1000) > exp) {
                    // token expired
                    console.log('re login');
                    context.commit('removeToken');
                } else if ((Date.now()/1000) > exp - 1800 && (Date.now()/1000) < orig_iat + 604800) {
                    // 1800 = 30 minutes
                    // 604800 = 7 days
                    // expires within 30 minutes and token is still within lifespan
                    console.log('refresh');
                    context.dispatch('refreshToken');
                } else {
                    // everything is normal, proceed to get course list
                    context.dispatch('getCourses');
                }
            }

            resolve();
        });


    }
};

const getters = {
    token () {
        return state.jwt;
    },
    loggedIn () {
        return !(state.jwt === undefined || state.jwt === null);
    }
};

export default {
    state,
    getters,
    actions,
    mutations
}