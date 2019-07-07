// set up axios
import axios from 'axios';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const $axios = axios.create({
      baseURL: 'http://127.0.0.1:8000/api/'
    });

export default $axios;