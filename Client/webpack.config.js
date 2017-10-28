const path    = require( 'path' )
const webpack = require( 'webpack' )

const HtmlWebpackPlugin = require( 'html-webpack-plugin' )
const MinifyPlugin      = require( 'babel-minify-webpack-plugin' )
const nodeExternals     = require( 'webpack-node-externals' )

const merge = require( 'webpack-merge' )

const resolve = source => {
  return path.resolve( __dirname, source )
}

const serverEntryPath = resolve( 'src/main.js' )
const clientEntryPath = resolve( 'src/public/main.js' )

const common = {
  devtool: 'source-map',
  resolve: {
    extensions: ['.js']
  },
  plugins: [new MinifyPlugin()],
  module: {
    loaders: [ {
      test   : /\.js$/,
      exclude: /node_modules/,
      loader : 'babel-loader',
      query  : {
        presets: ["stage-0", "stage-1", "stage-2", "stage-3", "es2015", "es2016", "es2017"]
      }
    } ]
  }
}

const backend = {
  entry: serverEntryPath,
  output: {
    path: resolve( 'dist' ),
    filename: 'server.js'
  },
  externals: [nodeExternals()],
  node: {
    __dirname: false
  },
  target: 'node'
}

const frontend = {
  entry: clientEntryPath,
  module: {
    rules: [{
      test: /\.elm$/,
      exclude: [/elm-stuff/, /node_modules/],
      use: 'elm-webpack-loader'
    }, {
      test: /\.(css|scss)$/,
      use: ['style-loader', {
        loader: 'css-loader',
        options: {
          minimize: true
        }
      }, 'sass-loader']
    }, {
      test: /\.(png|jpe?g|gif)$/,
      use: [{
        loader: 'file-loader',
        options: {
          name: '[name].[ext]',
          outputPath: 'resources/img/'
        }
      }]
    }]
  },
  plugins: [new HtmlWebpackPlugin()],
  output: {
    path: resolve( 'dist/public/' ),
    filename: 'client.js'
  }
}

module.exports = [
  merge( common, backend ),
  merge( common, frontend )
]
