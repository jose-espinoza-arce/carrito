(function() {
    'use strict';

    angular
        .module('app.service')
        .factory('order', order);

    order.$inject = ['$http','$q','baseUrl'];

    /* @ngInject */
    function order($http, $q, baseUrl) {

        var service = {
            sendNewOrder: sendNewOrder
        };

        return service;

        ////////////////

        function sendNewOrder(newOrder) {
            var defered = $q.defer(),
                promise = defered.promise;
            console.log(newOrder);
            var newOrder_string = JSON.stringify(newOrder);
            console.log(newOrder_string);
            $http.post(baseUrl + 'tags/upload/', newOrder_string, {
					headers: {
						//'Content-Type': undefined,
						"Authorization": "Token c4e913f4877e6762b8458b4d349ed402a5c3a842"
					},
					//transformRequest: angular.identify
				})
                .success(function(data) {
                    defered.resolve(data);
                })
                .error(function(data) {
                    defered.reject(data);
                });

            return promise;
        }
    }
})();