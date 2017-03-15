module.exports = {
  context: __dirname,
  entry: "./index.js",
  output: {
    path: "../slicer/static/",
    filename: "bundle.js"
  },
  module: {
    loaders: [
      {
        test: [/\.js?$/],
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015']
        }
      }
    ]
  },
  stats: {
            colors: true,
            modules: true,
            reasons: true,
            errorDetails: true
          },
  devtool: 'source-maps',
  resolve: {
    extensions: [".js"]
  }
};
