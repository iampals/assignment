(function () {

'use strict';
app.controller('indexController', ['$scope', '$location', 'authData','dataService', function ($scope, $location, authData, dataService) {

    $scope.headercontent={};

    function clearHeaderContent() {
        $scope.headercontent['companyheaderlogo']='';
        $scope.headercontent['navigationheaderslink1']='';
        $scope.headercontent['navigationheaderslink2']='';
        $scope.headercontent['personlogo']='';
        $scope.headercontent['personearn']='';
    }
    
    clearHeaderContent();

    $scope.logOut = function () {
        dataService.logOut();
        $location.path('/');
        clearHeaderContent();
    }
    $scope.authentication = authData.authenticationData;

    $scope.$on('headerupdate',function(evt,data){
        $scope.headercontent=data;
    })

}]);
})();