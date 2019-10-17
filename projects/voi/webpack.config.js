var path = require('path');
var webpack = require('webpack');
module.exports = {
  entry: {
    index:'./src/index.js',
  },
  output: {
    path: path.resolve(__dirname, "www/dist/js"),
    publicPath: "/dist/js/",
    filename: '[name].entry.js'
  },
  module: {
    // preLoaders is removed from the webpack^2.1.0-beta.23. See
    // https://github.com/MoOx/eslint-loader
    preLoaders: [
      {test: /\.js(x?)$/, loader: "eslint-loader", exclude: /node_modules/}
    ],
    loaders: [{
      test: /\.css$/, loader: "style-loader!css-loader?camelCase"
    },{
      test: /\.jsx$/,
      exclude: /node_modules/,
      loader: 'babel-loader',
      query: {
        presets: ['es2015','react']
      }
    },{
      test: /\.js$/,
      exclude: /node_modules/,
      loader: 'babel-loader',
      query: {
        presets: ['es2015']
      }
    }]
  },
  resolve: {
    extensions: ['', '.js', '.jsx']
  },
  devServer: {
    contentBase: "www/",
    historyApiFallback: {
      index: '/'
    }
  },
  debug: true,
  devtool: 'source-map',
  eslint: {
    configFile: './.eslintrc'
  },
};
