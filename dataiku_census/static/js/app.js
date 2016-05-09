var app = angular.module('myApp', []);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
})

app.controller('MainController', function ($scope, $http) {

    $scope.sortType = 'count'; // set the default sort type
    $scope.sortReverse = true; // set the default sort order
    $scope.limit = 100; // number of displayed results
    $scope.do_display = false;

    $scope.columns = [];
    $scope.stats = [];

    $scope.update = function () {
        $http.get('http://127.0.0.1:8000/stats/?q="' + $scope.selectedItem + '"')
            .then(function (response) {
                $scope.do_display = false;
                $scope.stats = response.data;
                if (response.data.length > 0) {
                    $scope.do_display = true;
                }
            });
    }

    $http.get("http://127.0.0.1:8000/columns/")
        .then(function (response) {
            $scope.columns = response.data.column_list;
        });
});