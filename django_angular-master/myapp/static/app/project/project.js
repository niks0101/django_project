'use strict';

angular.module('myApp.project', []).controller('ProjectCtrl', ['$scope', '$http', 'ProjectService', '$routeParams', function ($scope, $http, ProjectService, $routeParams) {
    console.log("ProjectCtrl intialized");
    $scope.project = {};
    $scope.files = [];
    $scope.dataLoading = true;
    //listen for the file selected event
    // $scope.$on("fileSelected", function (event, args) {
    //     $scope.$apply(function () {
    //         //add the file object to the scope's files collection
    //         $scope.files.push(args.file);
    //     });
    // });

    $scope.LoadFileData = function (files) {
        $scope.files.push(files[0]);
    };
    $scope.save = function() {
        $http({
            method: 'POST',
            url: "/Api/PostStuff",
            headers: { 'Content-Type': false },
            transformRequest: function (data) {
                var formData = new FormData();
                formData.append("questionset", angular.toJson(data.main_question));
                //now add all of the assigned files
                for (var i = 0; i < data.files; i++) {
                    //add each file to the form data and iteratively name them
                    formData.append("file" + i, data.files[i]);
                }
                return formData;
            },
            //Create an object that contains the model and files which will be transformed
            // in the above transformRequest method
            data: { questionset: $scope.main_question, files: $scope.files }
        }).
        success(function (data, status, headers, config) {
            alert("success!");
        }).
        error(function (data, status, headers, config) {
            alert("failed!");
        });
    };
    $scope.loadData=function() {
        ProjectService.GetProjectById($routeParams.id).then(function (responseData) {
            console.log(responseData);
            $scope.project = responseData;
            $scope.data = responseData.questionset;
            $scope.main_question =$scope.data[0];
        }, function (response) {
            FlashService.Error(response.message);
            $scope.dataLoading = false;
        });
    }
    $scope.showQuestions=function (id) {
        ProjectService.GetQuestionSet(id).then(function (responseData) {
                 $scope.main_question =responseData;
                }, function (response) {
                FlashService.Error(response.message);
                $scope.dataLoading = false;
        });
    }
    $scope.submitForm = function (question_id) {
        var question_id = question_id;
        var request = {
            method: 'POST',
            url: '/questionset/' + question_id+'/' ,
            headers: { 'Content-Type': undefined },
             transformRequest: function (data) {
                var formData = new FormData();
                formData.append("questionset", angular.toJson(data.questionset));
                for (var i in $scope.files) {
                formData.append("file", $scope.files[i]);
                }
                return formData;
            },
            data: { questionset: $scope.main_question, files: $scope.files }
        };
        ProjectService.UpdateQuestionSet(request).then(function (response) {
            console.log("success");
            $scope.loadData();
        }, function (errorresponse) {
            console.log("error");
        })
    };
    var formdata = new FormData();
    $scope.getTheFiles = function ($files) {
        angular.forEach($files, function (value, key) {
            formdata.append(key, value);
        });
    };
    $scope.loadData();
}]);
