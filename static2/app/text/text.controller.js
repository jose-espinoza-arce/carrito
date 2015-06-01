(function() {
	'use strict';

	angular
		.module('app.text')
		.controller('TextController', TextController);

	TextController.$inject = ['$scope', 'messages'];

	/* @ngInject */
	function TextController($scope, messages) {
		$scope.messages = messages;

		$scope.fontStacks = [{
			"name": "Arial",
			"stack": "sans-a"
		}, {
			"name": "Times New Roman",
			"stack": "serif-a"
		}, {
			"name": "Comic Sans MS",
			"stack": "sans-b"
		}, {
			"name": "Georgia",
			"stack": "serif-b"
		}];

		$scope.messages.headline = "Título va aquí";
		$scope.messages.font = $scope.fontStacks[0];
		$scope.messages.color = '#FFF';


	}
})();
