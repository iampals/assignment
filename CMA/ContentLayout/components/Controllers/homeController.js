(function () {
'use strict';
app.controller('homeController', ['$scope', 'dataService',function ($scope, dataService) {
   
    $scope.dashboarddata={};
    $scope.headercontent={};

    dataService.getPageContent().then(function (response) {
        if (response != null && response.error != undefined) {
            $scope.message = response.error_description;
        }
        else {
            $scope.dashboarddata=response;
            
            $scope.headercontent['companyheaderlogo']=response.companyheaderlogo;
            $scope.headercontent['navigationheaderslink1']=response.navigationheaderslink1;
            $scope.headercontent['navigationheaderslink2']=response.navigationheaderslink2;
            $scope.headercontent['personlogo']=response.personlogo;
            $scope.headercontent['personearn']=response.personearn;

            $scope.$emit('headerupdate',$scope.dashboarddata);
        }
    });

}]);

})();