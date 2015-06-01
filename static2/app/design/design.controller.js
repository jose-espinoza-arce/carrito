(function () {
    'use strict';

    angular
        .module('app.design')
        .controller('DesignController', DesignController);

    DesignController.$inject = ['$scope', '$state', '$stateParams', '$sessionStorage', 'designNetwork','order'];

    /* @ngInject */
    function DesignController($scope, $state, $stateParams, $sessionStorage, designNetwork, order) {

        $scope.title = 'DesignController';

        $scope.storage = $sessionStorage;

        $scope.design = designNetwork;

        $scope.imageLoaded = designNetwork.image;

        $scope.sendOrder = function (){
            console.log($scope.storage.order);
            order.sendNewOrder($scope.storage.order);
        };

        activate();

        ////////////////

        function activate() {

        }

        function orderExist() {
            return _.has($scope.storage, 'order');
        }
    }
})();
