(function() {
	'use strict';

	angular
		.module('app.type')
		.config(config);

	config.$inject = ['$stateProvider', '$urlRouterProvider'];

	function config($stateProvider, $urlRouterProvider) {
		$stateProvider
			.state('timeline.type', {
				url: '/type',
				templateUrl: 'static/app/type/type.html',
				controller: 'TypeController as vm'
			});
	}
})();
