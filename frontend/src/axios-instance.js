// set up axios
import axios from 'axios';
import settings from './settings';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const $axios = axios.create({
      baseURL: process.env.NODE_ENV === 'production' ? settings.domain + '/api/' : 'http://127.0.0.1:8000/api/'
    });

export default $axios;