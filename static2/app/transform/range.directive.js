(function () {
    "use strict";
    angular
        .module('app.transform')
        .directive('range', range);

    range.$inject = [];

    function range() {
        return {
            restrict: 'A',
            replace : true,
            template: '<div class="range"><div class="range__thumb"></div><div class="range__track"></div></div>',
            scope : {

            },
            link: link
        }
    }

    function link(scope, element, attrs){

    }

})();
