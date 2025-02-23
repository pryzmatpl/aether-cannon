/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        copper: '#B87333',
        brass: '#B5A642',
        steel: '#71797E',
      },
      fontFamily: {
        steampunk: ['Orbitron', 'sans-serif'],
      }
    },
  },
  plugins: [],
}