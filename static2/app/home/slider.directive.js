(function() {
	'use strict';

	angular
		.module('app.home')
		.directive('backslider', backslider);

	backslider.$inject = ['$compile', '$timeout'];

	/* @ngInject */
	function backslider($compile, $timeout) {
		// Usage:
		//
		// Creates:
		//
		var directive = {
			link: link,
			restrict: 'A',
			scope: {
				options: '=',
				source: '='
			}
		};
		return directive;

		function link(scope, element, attrs) {
			var bs = null;

			var defaultOptions = {
				mode: 'timer',
				effect: 'slidefade',
				effectTime: 1500,
				timerDelay: 10000,
				centerImages: true
			};

			if (scope.options) {
				angular.extend(defaultOptions, scope.options);
			}

			scope.$watch('source', function(newValue) {

				if (newValue) {
					$timeout(function() {
						bs = element.backslider(defaultOptions);
					}, 0);
				}

			});
		}
	}
})();
