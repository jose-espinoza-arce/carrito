(function () {
    'use strict';

    angular
        .module('app.upload')
        .controller('UploadController', UploadController);

    UploadController.$inject = ['$scope', '$rootScope', 'upload', 'designNetwork'];

    /* @ngInject */
    function UploadController($scope, $rootScope, upload, designNetwork) {

        $scope.upload = upload;
        $scope.image = {};

        $scope.design = designNetwork;

        // actions
        $scope.uploadFile = uploadFile;

        activate();

        ////////////////

        function activate() {
            console.log('UploadController');
        }

        function uploadFile() {
            var fd = new FormData();

            angular.forEach($scope.files, function (file) {
                fd.append('file', file);
            });

            upload.file(fd)
                .then(function (res) {
                    $scope.image = res;
                    $scope.design.setImage($scope.image);
                    //$rootScope.$broadcast('upload.complete');
                })
                .catch(function (err) {
                    console.log(err);
                });
        }
    }
})();
