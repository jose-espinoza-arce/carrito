(function() {
	'use strict';
	angular
		.module('app.summary')
		.config(config);

	config.$inject = ['$stateProvider'];

	function config($stateProvider) {
		$stateProvider
			.state('timeline.summary', {
				url: '/summary',
				templateUrl: 'static/app/summary/summary.html',
				controller: 'SummaryController as vm'
			});
	}
})();
