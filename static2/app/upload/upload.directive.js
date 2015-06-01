(function() {
	'use strict';

	angular
		.module('app.upload')
		.directive('fileInput', fileInput);

	fileInput.$inject = ['$parse'];

	/* @ngInject */
	function fileInput($parse) {
		// Usage:
		//
		// Creates:
		//
		var directive = {
			link: link,
			restrict: 'A'
		};
		return directive;

		function link(scope, element, attrs) {
			element.bind('change', function() {
				$parse(attrs.fileInput)
					.assign(scope, element[0].files);
				scope.$apply();
			});
		}
	}

})();
