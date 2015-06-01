(function () {
    "use strict";
    angular
        .module('app.transform')
        .controller('TransformController', TransformController);

    TransformController.$inject = ['$scope'];

    function TransformController($scope) {
        console.log('TransformController');
    }
})();