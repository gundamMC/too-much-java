const BundleTracker = require("webpack-bundle-tracker");
const settings = require('./src/settings');

module.exports = {
    publicPath: process.env.NODE_ENV === 'production' ? settings.domain + "/static/" : 'http://127.0.0.1:8080/',
    outputDir: './dist/',

    chainWebpack: config => {

        // config.optimization
        //     .splitChunks(true);

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: './webpack-stats.json'}]);

        config.resolve.alias
            .set('__STATIC__', 'static');

        config.devServer
            .public('http://0.0.0.0:8080')
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
