module.exports = {
     entry: './src/app.js',
     output: {
         path: './bin',
         filename: 'app.bundle.js'
     },
    module: {
         loaders: [{
             test: /\.js(x?)$/,
             exclude: /node_modules/,
             loader: 'babel-loader'
         }]
     },
   resolve: {
      
         extensions: ['', '.js', '.jsx']
          },
 };
