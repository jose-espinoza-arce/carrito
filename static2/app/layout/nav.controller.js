(function() {
  'use strict';

  angular
    .module('app.layout')
    .controller('NavController', NavController);

  NavController.$inject = ['types'];

  /* @ngInject */
  function NavController(types) {
    var vm = this;
    vm.title = 'NavController';

    vm.types = [];
    vm.date = new Date().getFullYear();


    activate();

    ////////////////

    function activate() {
      console.log(vm.title);
      var navigation = new Navigation();
      return getTypes();
    }

    function getTypes() {
      types
        .getAll()
        .then(function then(data) {
          console.log(data);
          vm.types = data;
        })
        .catch(function error(err) {
          console.log(err);
        });
    }

  }
})();
