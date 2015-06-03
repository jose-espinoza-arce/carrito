(function() {
	"use strict";
	angular
		.module('app.service')
		.factory('versions', versions);

	versions.$inject = ['$http', '$q', 'baseUrl'];

	function versions($http, $q, baseUrl) {

		return {
			allVersions: allVersions
		};

		function allVersions(id) {
			var defered = $q.defer(),
				promise = defered.promise;
			console.log(baseUrl + 'types/' + id + '/versions/');
			$http.get(baseUrl + 'types/' + id + '/versions/')
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
