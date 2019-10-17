var WebpackDevServer = require("webpack-dev-server");
var webpack = require("webpack");
var webConfig = require("../webpack.config");

var compiler = webpack(webConfig);
var devConfig = webConfig.devServer;
devConfig.publicPath = webConfig.output.publicPath;
var server = new WebpackDevServer(compiler, devConfig);
server.listen(8080, "0.0.0.0", function() {});