/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primaryPurpleColor: '#82328b',
        secondaryWhiteColor: '#f9f9f9',
        terciaryPurpleColor: '#4F4350',
        plusGrayColor: '#D9D9D9',
      }
    },
  },
  plugins: [],
}