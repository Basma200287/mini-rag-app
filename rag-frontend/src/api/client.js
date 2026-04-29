import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";
export const PROJECT_ID = 1;

const api = axios.create({
  baseURL: `${BASE_URL}/api/v1`,
  headers: { "Content-Type": "application/json" },
});
console.log('BASE_URL:', BASE_URL);
console.log('PROJECT_ID:', PROJECT_ID);
export default api;