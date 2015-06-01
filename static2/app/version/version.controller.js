(function () {
    'use strict';

    angular
        .module('app.version')
        .controller('VersionController', VersionController);

    VersionController.$inject = ['$state', '$stateParams', '$sessionStorage', 'versions', 'messages'];

    /* @ngInject */
    function VersionController($state, $stateParams, $sessionStorage, versions, messages) {
        var vm = this;
        vm.title = 'VersionController';
        vm.storage = $sessionStorage;
        vm.messages = messages;
        vm.versions = [];
        vm.version = null;
        vm.box = orderExist() ? vm.storage.order.item.box : 1;
        vm.save = save;
        vm.item = {};
        vm.order = {};
        vm.cycle = {index: 1, length: null};

        var typeid = orderExist() ? vm.storage.order.item.version.type : $stateParams.typeid;

        vm.messages.setTypeId(typeid);

        activate();

        ////////////////

        function activate() {
            if (!typeid) {
                $state.go('timeline.type');
            } else {
                return getVersions();
            }
        }

        function getVersions() {
            versions
                .allVersions(typeid)
                .then(function (versions) {

                    vm.versions = versions;

                    if (orderExist()) {
                        var indexVersion = _.findIndex(vm.versions, function (version) {
                            return version.id == vm.storage.order.item.version.id;
                        });
                        vm.version = versions[indexVersion];
                    } else {
                        vm.version = versions[0];
                    }
                })
                .catch(function (err) {
                    console.log(err);
                });
        }

        function orderExist() {
            return _.has(vm.storage, 'order');
        }

        function save() {

            vm.item.version = vm.version;
            vm.item.box = parseInt(vm.box, 10);
            vm.item.templates = [];
            vm.item.event = null;

            vm.cycle.length = vm.version.maxlabels * vm.item.box;

            vm.storage.order = {
                cycle: vm.cycle,
                item: vm.item
            };
        }
    }
})();
