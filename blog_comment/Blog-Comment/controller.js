var app = angular.module('app', []);
app.controller('main', ['$scope', function($scope){
  $scope.arrayComments = ["dxcfvgbhn","wertyui"];
    $scope.add = function () {
      //var input = $scope.comment;
      $scope.arrayComments.push($scope.comment);
      console.log($scope.arrayComments);
      $scope.comment = '';
    };
    $scope.click = function() {
     alert("Clicked!");
    };
}]);
