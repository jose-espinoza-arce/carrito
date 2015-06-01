(function() {
	'use strict';

	angular
		.module('app.type')
		.controller('TypeController', TypeController);

	TypeController.$inject = ['types' ,'$sessionStorage','messages'];

	/* @ngInject */
	function TypeController(types, $sessionStorage, messages) {
		var vm = this;
		vm.title = 'TypeController';
		vm.storage = $sessionStorage;
		vm.messages = messages;
		
		vm.storage.$reset();
		vm.messages.setTypeId(null);
		vm.types = [];
		activate();

		////////////////

		function activate() {
			console.log(vm.title);
			return getTypes();
		}

		function getTypes() {
			types
				.getAll()
				.then(function then(data) {
					vm.types = data;
				})
				.catch(function error(err) {
					console.log(err);
				});
		}
	}
})();
