(function() {
	'use strict';

	angular
	.module('app.event')
	.controller('EventController', EventController);

	EventController.$inject = ['$scope', '$state','$stateParams','$sessionStorage','events','templates','messages'];

	/* @ngInject */
	function EventController($scope, $state, $stateParams, $sessionStorage, events, templates, messages) {
		
		$scope.messages = messages;
		$scope.events = [];
		$scope.storage = $sessionStorage;

		$scope.getTemplates = getTemplates;

		$scope.templates = [];
		$scope.template = {};

		$scope.carousel;
		$scope.save = save;
		
		activate();

		////////////////

		function activate() {
			// there is a type of tequila parameter, but no order
			if ( !_.isUndefined($scope.messages.typeid) && !orderExist() ) {
				console.log($scope.messages.typeid);
					$state.go('timeline.version',{ typeid : $scope.messages.typeid});
			}else {
				return getEvents();
			}
		}

		function getEvents () {
			events
			.getAll()
			.then(function (data){
				$scope.events = data;
				$scope.event = data[1];
				$scope.getTemplates($scope.event.id);
			})
			.catch(function (error) {
				console.log(error);
			});
		}

		function getTemplates (eventId) {
			templates
			.getById(eventId)
			.then(function (data) {
				$scope.templates = data;
			})
			.catch(function (err) {
				console.log(err);
			});
		}

		function save (template) {
			$scope.storage.order.item.event = $scope.event;
			$scope.storage.order.item.templates[$scope.storage.order.cycle.index - 1] = template;
			console.log($scope.storage.order);
			
		}
		function orderExist () {
			return _.has($scope.storage, 'order');
		}
	}
})();
