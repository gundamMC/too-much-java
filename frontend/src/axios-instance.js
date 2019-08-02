// set up axios
import axios from 'axios';
import settings from './settings';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const $axios = axios.create({
      baseURL: settings.domain + '/api/'
    });

export default $axios;