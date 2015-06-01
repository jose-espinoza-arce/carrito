(function () {
    "use strict";

    function tqTransporter($compile, $timeout) {
        return {
            restrict: 'A',
            scope: {
                source: '=',
                storage : '='
            },
            link: function (scope, element, attrs) {
                var isInitiaLized = false,
                    elImage = element,
                    container = $('.image-preview');

                elImage.on('load', function () {

                        html2canvas(elImage.parent(), {

                            onrendered: function(canvas) {
                                document.body.appendChild(canvas);
                                scope.storage.order.item.tag = canvas.toDataURL();
                            }
                        });

                });

                scope.$watch("source", function (newValue) {

                    if(!_.isUndefined(newValue.file)){
                        elImage.attr('src', newValue.file);
                    }

                })
            }

        }
    }


    angular.module('app.design')
        .directive('tqTransporter', tqTransporter);

    tqTransporter.$inject = ['$compile', '$timeout'];

}());