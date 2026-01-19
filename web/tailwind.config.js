/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        heading: ['"Plus Jakarta Sans"', 'sans-serif'],
        body: ['"Plus Jakarta Sans"', 'sans-serif'],
      },
      colors: {
        bg: {
            primary: '#FAFAFA' // Warm off-white
        },
        text: {
            primary: '#1A2A3A',
            secondary: '#4A5A6A'
        },
        accent: {
            teal: '#1A5F7A',
            gold: '#D4A84B'
        }
      },
      borderRadius: {
        minimal: '16px'
      },
      boxShadow: {
        soft: '0 10px 30px rgba(0, 0, 0, 0.03)'
      },
      animation: {
        'fade-up': 'fadeUp 0.8s ease-out forwards',
      },
      keyframes: {
        fadeUp: {
            '0%': { opacity: '0', transform: 'translateY(20px)' },
            '100%': { opacity: '1', transform: 'translateY(0)' },
        }
      }
    },
  },
  plugins: [],
}
