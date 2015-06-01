(function() {
	'use strict';

	angular
		.module('app.summary')
		.controller('SummaryController', SummaryController);

	SummaryController.$inject = [];

	/* @ngInject */
	function SummaryController() {
		var vm = this;
		vm.title = 'DesignController';

		activate();

		////////////////

		function activate() {
			console.log(vm.title);
		}
	}
})();
