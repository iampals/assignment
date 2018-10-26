(function () {
    'use strict';
    app.service('dataService', ['$http', '$q', 'authData','$window',
    function ($http, $q, authData, $window) {

        var userInfo;
        var loginServiceURL = serviceBase + 'api/v1/loginusertoken/'//'api-token-auth/'
        var deferred;
        var tokenInfo;

        this.getTokenInfo = function () {
            return tokenInfo;
        }

        this.removeToken = function () {
            tokenInfo = null;
            $window.sessionStorage["TokenInfo"] = null;
        }

        this.init = function () {
            if ($window.sessionStorage["TokenInfo"]) {
                tokenInfo = $window.sessionStorage["TokenInfo"];
            }
        }

        this.getPageContent = function () {
            
            var url = serviceBase + 'api/v1/pages/1/';
            var deferred = $q.defer();
            
            var configRequest={
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
                    'Authorization' : 'JWT '+$window.sessionStorage["TokenInfo"]
                }
            };

            $http.get(url,configRequest).then(function (response) {
                deferred.resolve(response.data);
            }, function (error) {
                deferred.reject(error);
            });
            return deferred.promise;
        }

        this.login = function (userName, password) {
            deferred = $q.defer();
            var data = "grant_type=password&username=" + userName + "&password=" + password;
            $http.post(loginServiceURL, data, {
                headers:
                   { 'Content-Type': 'application/x-www-form-urlencoded' }
            }).success(function (response) {
                var o = response;
                userInfo = {
                    token: response.token,
                    userName: ""
                };

                $window.sessionStorage["TokenInfo"] = response.token;
                authData.authenticationData.IsAuthenticated = true;
                authData.authenticationData.userName = response.token;
                deferred.resolve(response);
            })
            .error(function (err, status) {
                authData.authenticationData.IsAuthenticated = false;
                authData.authenticationData.userName = "";
                deferred.resolve(err);
            });
            return deferred.promise;
        }

        this.logOut = function () {
            this.removeToken();
            authData.authenticationData.IsAuthenticated = false;
            authData.authenticationData.userName = "";
        }

        //this.init();
    }
    ]);
})();