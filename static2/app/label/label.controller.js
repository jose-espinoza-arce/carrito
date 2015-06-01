(function() {
	'use strict';

	angular
		.module('app.label')
		.controller('LabelController', LabelController);

	LabelController.$inject = ['$scope', '$rootScope', '$timeout', 'messages'];

	/* @ngInject */
	function LabelController($scope, $rootScope, $timeout, messages) {
		$scope.messages = messages;
		$scope.image = messages.image;
		$scope.filter = messages.filter;
		$scope.font = messages.font;

		var zoom;
		$scope.$on('upload.complete', function(event, args) {
			$timeout(function() {
				zoom = new Zoom();
				zoom.reset();

				var range = new Range({
					from: 1,
					to: 5,
					onStateChange: function(value) {
						zoom.scale(value);
					},
					onRangeLast: function(value) {
						zoom.lastRange(value);
					}
				});
				range.reset();
			}, 1000);
		});
	}
})();
