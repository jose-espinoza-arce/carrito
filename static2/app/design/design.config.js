(function() {
	'use strict';
	angular
		.module('app.design')
		.config(config);

	config.$inject = ['$stateProvider'];

	function config($stateProvider) {
		$stateProvider
			.state('timeline.design', {
				url: '/design',
				templateUrl: 'static/app/design/design.html',
				controller: 'DesignController'
			});
	}
})();
