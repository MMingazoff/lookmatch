import axios from "axios";
import router from "../route/route";

const api = axios.create({
    baseURL: "http://localhost:8000/api", // Replace with your API base URL
});

api.interceptors.request.use(
    (config) => {
        const accessToken = localStorage.getItem("accessToken");
        if (accessToken) {
            config.headers.Authorization = `Bearer ${accessToken}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

api.interceptors.response.use(
    (response) => {
        return response;
    },
    async (error) => {
        console.log(error)
        const originalRequest = error.config;
        const refreshToken = localStorage.getItem("refreshToken");
        if (
            error.response.status === 401 &&
            error.response.data.code === "token_not_valid" &&
            refreshToken &&
            !originalRequest._retry // Prevent infinite loop
        ) {
            try {
                const response = await axios.post(
                    "http://localhost:8000/api/users/login/refresh/", // Replace with your token refresh endpoint
                    {
                        refresh: refreshToken,
                    }
                );
                console.log(response.data.access)
                const newAccessToken = response.data.access;
                localStorage.setItem("accessToken", newAccessToken);
                originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
                return axios(originalRequest);
            } catch (error) {
                localStorage.removeItem("accessToken");
                localStorage.removeItem("refreshToken");
                await router.push({name: "Login"});
                return Promise.reject(error);
            }
        }
        return Promise.reject(error);
    }
);

export default api;
