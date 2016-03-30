var app = angular.module('app', ['ngRoute', 'ui.bootstrap']);

app.config(function ($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'html/homepage.html',
            controller: 'Homepage'
        })
        .when('/monitoring', {
            templateUrl: 'html/monitoring.html',
            controller: 'Monitoring'
        });
});