(function() {
	'use strict';

	angular
		.module('app.service')
		.factory('types', types);

	types.$inject = ['$http', '$q', 'baseUrl'];

	/* @ngInject */
	function types($http, $q, baseUrl) {
		var service = {
			getAll: getAll
		};
		return service;

		////////////////

		function getAll() {
			var defered = $q.defer(),
				promise = defered.promise;

			$http.get(baseUrl + 'types/')
				.success(function(data) {
					defered.resolve(data);
				})
				.error(function(err) {
					defered.reject(err);
				});

			return promise;
		}
	}
})();
