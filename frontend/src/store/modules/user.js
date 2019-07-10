import $axios from '../../axios-instance';

const state = {
    user: {}
};

const mutations = {
    updateUser(state, newUser){
        state.user = newUser
    },

    removeUser(state) {
        state.user = {};
    }
};

const actions = {
    getUser(context) {
        $axios
            .get('user/')
            .then(
                response => {
                    context.commit('updateUser', response.data);
                }
            );
    }
};

const getters = {
    user(state) {
        return state.user;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
}