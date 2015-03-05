var appControllers = angular.module('appControllers', ['user_mgmt']);

appControllers.controller('LoginCtrl', ['$scope', '$http', '$location', 'datastore',
  function ($scope, $http, $location, datastore) {
      if(window.user_id){ $location.path('/user/');}
      $scope.login_user = function () {
        $http.post('/', {'email': $scope.email, 'password': $scope.password}).
            success(function(data, status, headers, config){
                $scope.msg="Successfully Logged In";
                datastore.setId(data.id);
                $location.path('/user/');
            }).
            error(function (data, status, headers, config) {
                if(status == 404){$scope.msg="No user with this email &/or password found";}
                else{$scope.msg="Inactive User";}
            });
      };
  }]);

appControllers.controller('RegisterCtrl', ['$scope', '$http',
  function ($scope, $http) {
        $scope.addUser = function(){
            $scope.msg="";
            if ($scope.password != $scope.re_password){
                $scope.register_user.$valid = false;
                $scope.msg="Passwords don't match";
            }
            else{
                new_user = {'first_name': $scope.first_name, 'last_name': $scope.last_name, 'username': $scope.username,
                    'email': $scope.email, 'password': $scope.password, 're_password': $scope.re_password};
                $http.post('/users/', new_user).
                    success(function(data, status, headers, config){
                        $scope.msg = "Successfully Registered, you may login now";
                    }).
                    error(function (data, status, headers, config) {
                        if('email' in data){$scope.msg = "User with this email already exists."}
                        else{$scope.msg = data[0];}
                    });
            }
        };
  }]);

appControllers.controller('UserCtrl', ['$scope', '$http', '$location', 'datastore',
    function ($scope, $http, $location, datastore) {
        $scope.user_id = datastore.getId() || window.user_id;
        if(!$scope.user_id){$location.path('/');}
        $http.get('/users/'+$scope.user_id+'/').
            success(function(data, status, headers, config){
                $scope.first_name = data.first_name;
                $scope.last_name = data.last_name;
                $scope.email = data.email;
                $scope.username = data.username;
            }).
            error(function (data, status, headers, config) {
                if( status==404 ){$scope.msg = "An error occurred. Please login again";}
            });
        $scope.updateUser = function () {
            $http.put('/users/'+$scope.user_id+'/', {'first_name': $scope.first_name, 'last_name': $scope.last_name}).
                success(function(data, status, headers, config){
                    $scope.msg = "Details Successfully Updated";
                }).
                error(function(data, status, headers, config){
                    $scope.msg = "Error in updating details";
                });
        };
        $scope.logout = function(){
            $http.get('/logout').
                success(function(data, status, headers, config){
                    window.user_id="";
                    $scope.user_id = "";
                    $location.path('/');
                }).
                error(function(data , status, headers, config){});
        };
}]);