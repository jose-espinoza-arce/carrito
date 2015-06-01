var Navigation = (function($) {
	var leftMenu = $('.left-bar'),
		triggerMenu = leftMenu.find('a.logo__image'),
		thin = leftMenu.find('div.left-bar__thin'),
		logo = leftMenu.find('div.logo'),
		wide = leftMenu.find('div.left-bar__wide'),
		overlay = leftMenu.find('div.left-bar__overlay'),
		closeButton = leftMenu.find('div.close-button'),
		isOpen = false,
		timeline = null;

	function Navigation() {
		initialize();
	}

	// Public API
	Navigation.prototype.spread = function() {
		timeline.reverse();
		isOpen = false;
	};

	Navigation.prototype.folded = function() {
		timeline.play();
		isOpen = true;
	};

	// Initialize

	function initialize() {
		timeline = new TimelineMax();
		timeline
			.to(logo, 0.3, {
				rotationY: '-90deg'
			})
			.to(thin, 0.1, {
				left: -50
			})
			.to(overlay, 0.1, {
				display: 'block'
			})
			.to(overlay, 0.2, {
				opacity: 0.7
			})
			.to(wide, 0.3, {
				left: 0
			})
			.to(closeButton, 0.3, {
				left: 700
			})
			.to(closeButton, 0.3, {
				rotationY: '0deg'
			});
		timeline.stop();

		// listen spread/folded
		triggerMenu.on('click', function(e) {
			e.preventDefault();

			isOpen = !isOpen;
			leftMenu.toggleClass('left-bar--collapsed');

			if (isOpen === true) {
				timeline.play();
			} else {
				timeline.reverse();
			}

			return false;

		});
	}

	return Navigation;
})(jQuery);
