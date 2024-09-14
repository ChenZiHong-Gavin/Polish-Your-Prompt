import { create } from "zustand";

const useGenerateStore = create((set) => ({
    status: "idle",
    generated: "",
    setStatus: (val) => set({ status: val }),
    setGenerated: (val) => set({ generated: val }),
}));

const useQueryAndSchemaAndModeStore = create((set) => ({
    query: "",
    schema: "",
    mode: "ONE_STEP",
    setQuery: (val) => set({ query: val }),
    setSchema: (val) => set({ schema: val }),
    setMode: (val) => set({ mode: val }),
}));

const useCheckedSchemaStore = create((set) => ({
    checkedSchema: 0,
    setCheckedSchema: (val) => set({ checkedSchema: val }),
}));

const useCheckedModeStore = create((set) => ({
    checkedMode: "ONE_STEP",
    setCheckedMode: (val) => set({ checkedMode: val }),
}));


export { useGenerateStore, useQueryAndSchemaAndModeStore, useCheckedSchemaStore, useCheckedModeStore };