(function() {
	'use strict';

	angular
		.module('app.filter')
		.controller('FilterController', FilterController);

	FilterController.$inject = ['$scope', 'messages'];

	/* @ngInject */
	function FilterController($scope, messages) {
		$scope.messages = messages;

	}
})();
