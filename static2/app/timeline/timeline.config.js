(function() {
	'use strict';
	angular
		.module('app.timeline')
		.config(config);

	config.$inject = ['$stateProvider', '$urlRouterProvider'];

	function config($stateProvider, $urlRouterProvider) {
		$stateProvider
			.state('timeline', {
				url: '/timeline',
				templateUrl: 'static/app/timeline/timeline.html',
				controller: 'TimelineController as vm'
			});
	}
})();
