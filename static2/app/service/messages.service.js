(function() {
	'use strict';

	angular
		.module('app.service')
		.factory('messages', messages);


	/* @ngInject */
	function messages() {
		var service = {
			typeid : null,
			filter    : {},
			image     : {},
			font      : {},
			setTypeId : setTypeId,
			addImage  : addImage,
			addFilter : addFilter,
			addFont   : addFont
		};
		return service;

		////////////////

		function addImage(image) {
			service.image = image;
		}

		function addFilter(filter) {
			service.filter = filter;
		}

		function addFont(font) {
			service.font = font;
		}

		function setTypeId (id) {
			service.typeid = id;
		}
	}
})();
