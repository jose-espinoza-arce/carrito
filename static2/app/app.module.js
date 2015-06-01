(function () {
    'use strict';

    angular
        .module('app', [
            'app.core',
            'app.service',
            'app.layout',
            'app.home',
            'app.timeline',
            'app.type',
            'app.version',
            'app.event',
            'app.design',
            'app.upload',
            'app.transform',
            'app.label',
            'app.filter',
            'app.customtext',
            'app.summary'
        ])
        .config(config);

    config.$inject = ['$stateProvider', '$urlRouterProvider'];

    function config($stateProvider, $urlRouterProvider) {
        $stateProvider
            .state('home', {
                url: '/home',
                templateUrl: 'app/home/home.html',
                controller: 'HomeController as vm'
            });
        $urlRouterProvider.otherwise('/timeline/type');
    }
})();
