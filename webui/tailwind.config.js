/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'node_modules/daisyui/dist/**/*.js',
    'node_modules/react-daisyui/dist/**/*.js',
    "./index.html",
    "./src/**/*.js"
  ],
  theme: {
    extend: {},
  },
  daisyui: {
    themes: ["light", "dark", "'emerald", "lemonade", "retro"],
  },
  plugins: [require('daisyui')],
};

