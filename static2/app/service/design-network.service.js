(function () {
    "use strict";
    angular
        .module('app.service')
        .factory('designNetwork', designNetwork);

    function designNetwork(){

        var service = {
            // transporter loaded image
            image: {},
            setImage: setImage,

            font: {},
            setFont: setFont
        };
        return service;

        ////////////////

        function setFont(font) {
            service.font = font;
        }

        function setImage(image) {
            service.image = image;
        }
    }
}());
