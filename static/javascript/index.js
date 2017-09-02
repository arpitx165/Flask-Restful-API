(function () {

  'use strict';

  angular.module('node', [])

  .controller('mainController', ['$scope', '$log', '$http',
    function($scope, $log, $http) {
      $scope.tech_repos=true
      $scope.user_profile=true
      $scope.tech_name= false;
      console.log("hello");

      $http.get('technology').then((res)=>{
        console.log(res.data.data);
        $scope.tech = [];
        for (var i = 0; i < res.data.data.Count.length; i++) {
          if (res.data.data.language_Name[i] == null) continue;
          var json = { tech : res.data.data.language_Name[i], count : res.data.data.Count[i]}
          $scope.tech.push(json);
        }
      })


$scope.repos = []

$scope.goBack = function(){
  $scope.tech_repos=true
  $scope.user_profile=true
  $scope.tech_name= false;
}
 $scope.showList = function (b) {
  console.log(b);
  $http.get('repo/'+ encodeURIComponent(b)).then((res)=>{
    console.log(res.data.response.data.repos.length);
    $scope.repos = res.data.response.data.repos;
    $scope.tech_repos=false
    $scope.tech_name= true;
  })
}

$scope.repos = []
 $scope.showUser = function (b) {
  console.log(b);
  $http.get('user/'+ encodeURIComponent(b)).then((res)=>{
    console.log(res.data);
    $scope.owner = res.data.response.data.repos;
    $scope.tech_repos=true
    $scope.user_profile=false
  })
}
}

  ]);

}());
