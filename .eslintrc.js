module.exports = {
  "env": {
    "node": true,
    "es6": true
  },
  "extends": "standard",
  "parserOptions": {
    "sourceType": "module",
    "ecmaVersion": 8
  },
  "rules": {
    "semi": ["error", "never"],
    "prefer-arrow-callback": "error",
    "no-var": "error",
    "prefer-template": "error"
  }
}
