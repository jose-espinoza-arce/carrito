(function() {
    'use strict';

    angular
        .module('app.service')
        .factory('templates', templates);

    templates.$inject = ['$http','$q','baseUrl'];

    /* @ngInject */
    function templates($http, $q, baseUrl) {
        var service = {
            getById: getById
        };
        return service;

        ////////////////

        function getById(eventId) {
          var
            defered = $q.defer(),
            promise = defered.promise;

          $http.get(baseUrl + 'events/' + eventId + '/templates/')
            .success(function (data){
              defered.resolve(data);
            })
            .error(function (err){
              defered.reject(err);
            });
          return promise;
        }
    }
})();