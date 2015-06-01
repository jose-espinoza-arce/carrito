(function() {
	'use strict';

	angular
		.module('app.service')
		.factory('upload', upload);

	upload.$inject = ['$http', '$q', 'baseUrl'];

	/* @ngInject */
	function upload($http, $q, baseUrl) {

		var service = {
			file: file
		};

		return service;

		////////////////

		function file(fd) {
			var defered = $q.defer(),
				promise = defered.promise;

			$http.post(baseUrl + 'customimages/', fd, {
					headers: {
						'Content-Type': undefined,
						"Authorization": "Token c4e913f4877e6762b8458b4d349ed402a5c3a842"
					},
					transformRequest: angular.identify
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
