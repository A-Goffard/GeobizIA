module.exports = {
  root: true,
  env: {
    node: true,
    'vue/setup-compiler-macros': true, // La clave para defineProps/Emits
  },
  extends: [
    'plugin:vue/vue3-essential',
    'eslint:recommended',
  ],
  // Especifica el parser correcto para archivos .vue y su contenido
  parser: 'vue-eslint-parser',
  parserOptions: {
    parser: '@babel/eslint-parser', // El parser para los bloques <script>
    sourceType: 'module',
    ecmaVersion: 2021,
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'vue/multi-word-component-names': 'off', // Permite nombres de componente de una sola palabra
  },
};
