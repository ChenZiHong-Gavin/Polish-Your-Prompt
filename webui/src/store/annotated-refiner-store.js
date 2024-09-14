import { create } from "zustand";

const useGenerateStore = create((set) => ({
    status: "idle",
    generated: "",
    setStatus: (val) => set({ status: val }),
    setGenerated: (val) => set({ generated: val }),
}));

const useQueryAndContentAndAnnotations = create((set) => ({
    query: "",
    content: "",
    annotations: "",
    setQuery: (val) => set({ query: val }),
    setContent: (val) => set({ content: val }),
    setAnnotations: (val) => set({ annotations: val }),
}));


export { useGenerateStore, useQueryAndContentAndAnnotations };