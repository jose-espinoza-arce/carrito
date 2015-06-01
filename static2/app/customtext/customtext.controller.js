(function () {
    "use strict";
    angular
        .module('app.customtext')
        .controller('CustomTextController',CustomTextController);

    CustomTextController.$inject = ['$scope', 'designNetwork'];

    function CustomTextController($scope , designNetwork) {

        $scope.title = 'CustomTextController';

        $scope.design = designNetwork;

        $scope.fontStack = [{
            "name": "Arial",
            "stack": "sans-a"
        }, {
            "name": "Times New Roman",
            "stack": "serif-a"
        }, {
            "name": "Comic Sans MS",
            "stack": "sans-b"
        }, {
            "name": "Georgia",
            "stack": "serif-b"
        }];

        ////////////////

        function active() {
            console.log($scope.title);

            $scope.design.headline = "Título va aquí";
            $scope.design.font = $scope.fontStack[0];
            $scope.design.color = '#FFF';
        }
        active();
    }
}());
