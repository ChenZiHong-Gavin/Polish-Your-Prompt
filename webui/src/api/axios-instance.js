import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: 'http://localhost:8000',
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json',
    },
});


axiosInstance.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        // apiBase and apiKey are stored in localStorage
        const apiBase = localStorage.getItem('apiBase');
        const apiKey = localStorage.getItem('apiKey');
        if (apiBase && apiKey) {
            config.headers['x-api-base'] = apiBase;
            config.headers['x-api-key'] = apiKey;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

axiosInstance.interceptors.response.use(
    (response) => {
        return response.data;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default axiosInstance;