module.exports = {
  root: true,
  parser: 'babel-eslint',
  parserOptions: {
    sourceType: 'module'
  },
  env: {
    browser: true
  },
  // https://github.com/feross/standard/blob/master/RULES.md#javascript-standard-style
  extends: 'standard',
  // required to lint *.wpy files
  plugins: [
    'html'
  ],
  settings: {
    'html/html-extensions': ['.html', '.wpy']
  },
  // add your custom rules here
  'rules': {
    // allow paren-less arrow functions
    'arrow-parens': 0,
    // allow async-await
    'generator-star-spacing': 0,
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
    "max-len": [
      "warn", // type of result
      100, // max len
      2 // tabwidth
    ],
    "no-tabs": ["warn"],
    "eqeqeq": ["error", "smart"],
    "no-trailing-spaces": ["error"],
    "no-whitespace-before-property": "error",
    "no-multi-spaces": "error",
    "no-console": ["error", { "allow": ["log"] }], // for dev
    "space-before-blocks": "error",
    "space-before-function-paren": ["error",
      {"anonymous": "always", "named": "never", "asyncArrow": "always"}],
    "space-in-parens": ["error", "never"],
    "space-infix-ops": "error",
    "space-unary-ops": [
      2, {
        "words": true,
        "nonwords": false
      }],
    "spaced-comment": ["error", "always"],
    "keyword-spacing": ["error"],
    "no-unexpected-multiline": "error",
    "semi": ["error", "never"],
    "indent": ["warn", 2],
    "no-unused-vars": ["warn", { "args": "none" }]
  }
}
