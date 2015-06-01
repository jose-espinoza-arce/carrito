(function () {
    'use strict';

    angular
        .module('app.timeline')
        .controller('TimelineController', TimelineController);

    TimelineController.$inject = [];

    /* @ngInject */
    function TimelineController() {
        var vm = this;
        vm.title = 'TimelineController';
        vm.states = [{
            step: 1,
            url: 'type',
            label: 'Tequila'
        }, {
            step: 2,
            url: 'version',
            label: 'Version'
        }, {
            step: 3,
            url: 'event',
            label: 'Evento'
        }, {
            step: 4,
            url: 'design',
            label: 'Diseño'
        }, {
            step: 5,
            url: 'summary',
            label: 'Resumen'
        }];

        activate();

        ////////////////

        function activate() {
            console.log(vm.title);
        }
    }
})();
