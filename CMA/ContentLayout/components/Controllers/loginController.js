(function () {
    'use strict';
    app.controller('loginController', ['$scope', 'dataService', '$location', function ($scope, dataService, $location) {

        $scope.loginData = {
            userName: "",
            password: ""
        };

        $scope.login = function () {
            dataService.login($scope.loginData.userName, $scope.loginData.password).then(function (response) {
                if (response != null && response.error != undefined) {
                    $scope.message = response.error_description;
                }
                else {
                    $location.path('/home');
                }
            });
        }
    }]);
})();