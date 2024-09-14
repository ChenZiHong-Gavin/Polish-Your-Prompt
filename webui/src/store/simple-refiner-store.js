import { create } from "zustand";

const useGenerateStore = create((set) => ({
    status: "idle",
    generated: "",
    setStatus: (val) => set({ status: val }),
    setGenerated: (val) => set({ generated: val }),
}));

const usePrefixAndQueryStore = create((set) => ({
    prefix: "",
    query: "",
    setPrefix: (val) => set({ prefix: val }),
    setQuery: (val) => set({ query: val }),
}));


export { useGenerateStore, usePrefixAndQueryStore };