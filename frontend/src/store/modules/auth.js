import $axios from '../../axios-instance';
import jwt_decode from 'jwt-decode';
import router from '../../router';

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
    refreshToken() {
        const payload = {
            token: state.jwt
        }
        $axios.post(state.endpoints.refreshJWT, payload)
            .then((response) => {
                this.commit('updateToken', response.data.token)
            })
            .catch((error) => {
                console.log(error)
            })
    },
    inspectToken(){
      const token = state.jwt;
      if(token){
        const decoded = jwt_decode(token);
        const exp = decoded.exp;
        const orig_iat = decoded.orig_iat;
        if(exp - (Date.now()/1000) < 1800 && (Date.now()/1000) - orig_iat < 628200){
            // Token within lifespan, simply refresh
          this.dispatch('refreshToken')
        } else if (exp -(Date.now()/1000) < 1800){
          // DO NOTHING, DO NOT REFRESH
        } else {
          // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
        }
      }
    }
};

const getters = {
    token () {
        return state.jwt;
    }
};

export default {
    state,
    getters,
    actions,
    mutations
}