(function() {
	'use strict';
	angular
		.module('app.version')
		.config(config);

	config.$inject = ['$stateProvider'];

	function config($stateProvider, $urlRouterProvider) {
		$stateProvider
		/*.state('timeline.version', {
			url: '/version',
			templateUrl: 'app/version/version.html',
			controller: 'VersionController as vm'
		})*/
			.state('timeline.version', {
			url: '/version/:typeid',
			templateUrl: 'static/app/version/version.html',
			controller: 'VersionController as vm'
		});
	}
})();
