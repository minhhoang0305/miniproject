import axios from "axios"

const baseURL = import.meta.env.VITE_API_URL?.replace(/\/$/, "")

console.log("Axios baseURL:", baseURL)

const api = axios.create({
    baseURL: baseURL || "http://localhost:8000",
    headers: {
        "Content-Type": "application/json",
    },
})

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem("access")
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error) => {
        return Promise.reject(error)
    }
)

export default api
