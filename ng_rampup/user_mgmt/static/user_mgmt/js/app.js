/**
 * Created by ubuntu on 26/2/15.
 */
(function(){
    var app = angular.module('user_mgmt', ["ngRoute", "appControllers"]);


    app.config(['$routeProvider', '$httpProvider',
        function($routeProvider, $httpProvider) {
            $routeProvider.
                when('/register', {
                    templateUrl: 'static/user_mgmt/register.html',
                    controller: 'RegisterCtrl'
                }).
                when('/', {
                    templateUrl: 'static/user_mgmt/login.html',
                    controller: 'LoginCtrl'
                }).
                when('/user', {
                    templateUrl: 'static/user_mgmt/user_detail.html',
                    controller: 'UserCtrl'
                }).
                otherwise({
                    redirectTo: '/'
                });
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        }]);

    app.factory("datastore", function () {
        var object = {};
        object.id = "";
        object.getId = function () {
          return this.id;
        };
        object.setId = function (id) {
            this.id = id;
        };
        return object;
    });
})();

