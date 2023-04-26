const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
    app.use(
        '/json_files',
        createProxyMiddleware({
        target: 'http://localhost:3002/',
        pathRewrite: {
            '^/json_files': '/'
        }
        })
    );
};
