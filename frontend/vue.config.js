const BundleTracker = require("webpack-bundle-tracker");
import settings from './src/settings';

module.exports = {
    publicPath: process.env.NODE_ENV === 'production' ? settings.domain + "/static/" : '127.0.0.1:8080',
    outputDir: './dist/',

    chainWebpack: config => {

        config.optimization
            .splitChunks(false);

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: './webpack-stats.json'}]);

        config.resolve.alias
            .set('__STATIC__', 'static');

        config.devServer
            .public('127.0.0.1:8080')
            .host('0.0.0.0')
            .port(8080)
            .historyApiFallback(true)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .headers({"Access-Control-Allow-Origin": ["\*"]});

    },

    // pages: {
    //     index: 'src/main.js',
    //     test_page: 'src/test_page.js'
    // }

};
