(function() {
	'use strict';
	angular
		.module('app.event')
		.config(config);

	config.$inject = ['$stateProvider'];

	function config($stateProvider) {
		$stateProvider
			.state('timeline.event', {
				url: '/event',
				templateUrl: 'static/app/event/event.html',
				controller: 'EventController'
			});
	}
})();
