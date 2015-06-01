(function() {
	'use strict';

	angular
		.module('app.home')
		.controller('HomeController', HomeController);

	HomeController.$inject = [];

	/* @ngInject */
	function HomeController() {
		var vm = this;
		vm.title = 'HomeController';

		vm.slides = [{
			heading: "Tu momento especial",
			text: "Porque siempre hay esa canción, aroma, lugar que lo revive.",
			image: 'images/slides/1.jpg',
			action: 'Comience ahora',
			position: 'top-left'
		}, {
			heading: "Transfórmalo",
			text: "Esa fotografía tomada por el corazón.",
			image: 'images/slides/2.jpg',
			action: 'No esperes más',
			position: 'top-right'
		}, {
			heading: "A un recuerdo eterno",
			text: "Conservar es asegurar que no se olvide.",
			image: 'images/slides/3.jpg',
			action: 'Envíe su pedido hoy',
			position: 'top-right'
		}];

		activate();

		////////////////

		function activate() {
			console.log(vm.title);
		}
	}
})();
