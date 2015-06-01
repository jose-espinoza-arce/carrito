(function(){
    'use strict';
    angular
      .module('app.service')
      .factory('events', events);

  events.$inject = ['$http', '$q', 'baseUrl'];

  function events ($http, $q, baseUrl) {
    var service = {
      getAll : getAll
    };
    return service;

    function getAll () {
      var
        defered = $q.defer(),
        promise = defered.promise;

      $http.get(baseUrl + 'events/')
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