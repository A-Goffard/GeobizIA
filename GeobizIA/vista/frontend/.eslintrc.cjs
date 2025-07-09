/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution');

module.exports = {
  root: true,
  // Especifica el entorno. 'vue/setup-compiler-macros' es la clave para defineProps/Emits.
  env: {
    browser: true,
    es2021: true,
    node: true,
    'vue/setup-compiler-macros': true
  },
  // Usa las reglas recomendadas para Vue 3.
  extends: [
    'plugin:vue/vue3-recommended',
    'eslint:recommended'
  ],
  // Configuración del parser para que entienda la sintaxis de Vue y ES moderno.
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  rules: {
    // Puedes añadir reglas personalizadas aquí si lo necesitas.
    // Por ahora, lo dejamos vacío para usar las recomendaciones.
    'vue/multi-word-component-names': 'off', // Desactiva la regla que obliga a nombres de componente con varias palabras
  }
};
