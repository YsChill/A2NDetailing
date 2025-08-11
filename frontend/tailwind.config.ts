/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}",],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        accent: "#7B2A2A",
        charcoal: "#1a1a1a",
      },
    },
  },
  plugins: [],
}

