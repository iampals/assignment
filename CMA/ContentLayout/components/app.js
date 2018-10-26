var serviceBase = 'http://localhost:8000/';

var app = angular.module('orgAssessment', ['ngRoute']);

app.config(function ($routeProvider) {

    $routeProvider.when("/home", {
        controller: "homeController",
        templateUrl: "/components/views/home.html"
    });

    $routeProvider.when("/login", {
        controller: "loginController",
        templateUrl: "/components/views/login.html"
    });

   // $routeProvider.otherwise({ redirectTo: "/home" });

})
    .config(['$httpProvider', function ($httpProvider) {

        $httpProvider.interceptors.push(function ($q, $rootScope, $window, $location) {

            return {
                request: function (config) {
                    return config;
                },
                requestError: function (rejection) {

                    return $q.reject(rejection);
                },
                response: function (response) {
                    if (response.status == "401") {
                        $location.path('/login');
                    }
                    return response;
                },
                responseError: function (rejection) {

                    if (rejection.status == "401") {
                        $location.path('/login');
                    }
                    return $q.reject(rejection);
                }
            };
        });
    }]);