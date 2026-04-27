import api, { PROJECT_ID } from "./client";

/* ─────────────────────────────
   👤 USER - QUESTION ANSWER
───────────────────────────── */
export const askQuestion = (question) =>
  api.post(`/nlp/index/answer/${PROJECT_ID}`, { question });


/* ─────────────────────────────
   🛠️ ADMIN - UPLOAD DOCUMENT
───────────────────────────── */
export const uploadDocument = (formData) =>
  api.post(`/data/upload/${PROJECT_ID}`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });


/* ─────────────────────────────
   ⚙️ ADMIN - PROCESS DOCUMENTS
───────────────────────────── */
export const processDocuments = () =>
  api.post(`/data/process/${PROJECT_ID}`);


/* ─────────────────────────────
   📚 ADMIN - INDEX DOCUMENTS
───────────────────────────── */
export const indexDocuments = () =>
  api.post(`/nlp/index/push/${PROJECT_ID}`);


/* ─────────────────────────────
   📊 ADMIN - INDEX INFO
───────────────────────────── */
export const getIndexInfo = () =>
  api.get(`/nlp/index/info/${PROJECT_ID}`);


/* ─────────────────────────────
   🔍 SEARCH INDEX
───────────────────────────── */
export const searchIndex = (query) =>
  api.post(`/nlp/index/search/${PROJECT_ID}`, { query });