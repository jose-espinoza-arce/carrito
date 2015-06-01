var Range = (function(window, $, undefined) {

	var
		defaults = {
			from: 1,
			to: 10,
			step: 1,
			el: '.range',
			onStateChange: function(value) {},
			onRangeLast: function(value) {}
		},
		rangeValue = 1,
		options = {},
		$el, el, thumb, track = null,
		isTouchSupported = false,
		events = {},
		offsetX = 0,
		bound = {};
	lastValue = 1;

	function Range(opts) {
		// parse options
		options = $.extend({}, defaults, opts || {});

		// initialize module
		initialize();
	}

	Range.prototype.reset = function() {
		thumb.css({
			left: 0
		});

		rangeValue = 1;

		options.onStateChange({
			value: rangeValue,
			from: options.from,
			to: options.to
		});

		removeListeners();

		initialize();

	};

	var initialize = function() {

		// check touch support
		if (('ontouchstart' in window) || window.DocumentTouch && document instanceof DocumentTouch) {
			isTouchSupported = true;
		}

		// that events should be used
		events = (isTouchSupported ? {
			start: 'touchstart',
			end: 'touchend',
			move: 'touchmove'
		} : {
			start: 'mousedown',
			end: 'mouseup',
			move: 'mousemove'
		});

		// jquery el ref
		$el = ($(options.el).length) ? $(options.el) : $(defaults.el);
		// dom el ref
		el = $el[0];

		// jquery thumb
		thumb = $el.find('.range__thumb');

		// track thumb
		track = $el.find('.range__track');

		// check bound box to clamp thumb
		bound = {
			left: track.position().left,
			right: track.width() - thumb.width()
		};

		// initialize listeners
		addListeners();

	};

	var addListeners = function() {
		thumb.on(events.start, onStartHandler);
	};

	var removeListeners = function() {
		thumb.off(events.start, onStartHandler);
		$(document).off(events.move, onMoveHandler);
		$(document).off(events.end, onEndHandler);
	};

	var onStartHandler = function(evt) {
		evt.preventDefault();

		// where is the mouse respect to thumb
		offsetX = getPosition(evt).x - thumb.position().left;

		// add Listeners
		$(document).on(events.end, onEndHandler);
		$(document).on(events.move, onMoveHandler);
	};

	var onEndHandler = function() {
		// remove listeners
		$(document).off(events.move, onMoveHandler);
		$(document).off(events.end, onEndHandler);

		options.onRangeLast({
			value: rangeValue,
			from: options.from,
			to: options.to
		});

		lastValue = rangeValue;

	};

	var onMoveHandler = function(evt) {
		var point = getPosition(evt),
			intrinsicProportion = (options.to - options.from) / (bound.right - bound.left),
			thisPoint = (point.x - offsetX),
			newPoint = clamp(thisPoint, bound.left, bound.right);

		rangeValue = (thisPoint - bound.left) * intrinsicProportion + options.from;

		// drag thumb
		thumb.css({
			left: newPoint
		});

		// value to dispatch
		rangeValue = clamp(rangeValue, options.from, options.to);

		options.onStateChange({
			value: rangeValue,
			last: lastValue,
			from: options.from,
			to: options.to
		});

	};

	// get mouse/touch position
	var getPosition = function(evt) {
		var posX = 0,
			posY = 0;

		if (evt.originalEvent.targetTouches) {
			posX = evt.originalEvent.targetTouches[0].pageX;
			posY = evt.originalEvent.targetTouches[0].pageY;
		} else if (evt.pageX || evt.pageY) {
			posX = evt.pageX;
			posY = evt.pageY;
		} else if (evt.clientX || evt.clientY) {
			posX = evt.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
			posY = evt.clientY + document.body.scrollTop + document.documentElement.scrollTop;
		}

		return {
			x: posX,
			y: posY
		};
	};

	// clamp helper
	var clamp = function(value, min, max) {
		return Math.min(Math.max(value, min), max);
	};

	// expose the module
	return Range;

})(window, jQuery);
