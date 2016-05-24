require([
    'jquery',
    'views/page-view',
    'views/form',
    'bootstrap-nifty',
    'knockout',
    'plugins/knockout-select2'
], function($, PageView, Form) {
    /**
     * a view to manage configuration settings for the app
     * @augments PageView
     * @constructor
     * @name ConfigManager
     */
    return new PageView({
        viewModel: {
            form: new Form({
                el: $('.arches-form')[0],
                modelName: 'config'
            })
        }
    });
});
