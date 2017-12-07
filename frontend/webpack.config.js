module.exports = {
  entry: './app.js',
  output: {
    filename: 'bundle.js'
  }
};

const config = {
  entry: {
    Home: './src/home/index.js',
    single_product: './src/single_product/index.js'
  }
};