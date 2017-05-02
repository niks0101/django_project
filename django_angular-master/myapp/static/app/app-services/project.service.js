/**
 * Created by Apple on 1/31/17.
 */
(function () {
    'use strict';

    angular
        .module('myApp')
        .factory('ProjectService', ProjectService);

    ProjectService.$inject = ['$http'];
    function ProjectService($http) {
        var service = {};

        service.GetAllProjects = GetAllProjects;
        service.GetProjectById = GetProjectById;
        service.GetQuestionSet=GetQuestionSet;
        service.UpdateQuestionSet = UpdateQuestionSet;
        service.DeleteProject = Delete;
        service.setAnswer=setAnswers;
        service.CreateProject = Create;

        return service;

        function GetAllProjects() {
            return $http.get('/projects').then(handleSuccess, handleError('Error getting all projects'));
        }

        function GetProjectById(id) {
            return $http.get('/projects/' + id+'/').then(handleSuccess, handleError('Error getting project by id'));
        }
        function GetQuestionSet(questionid) {
            return $http.get('/questionset/'+questionid+'/').then(handleSuccess, handleError('Error getting project by id'));
        }

        function UpdateQuestionSet(request) {
             return $http(request).then(handleSuccess, handleError('Error while setting answers'));
        }

        function setAnswers(request) {
            return $http(request).then(handleSuccess, handleError('Error while setting answers'));
        }

        function Create(project) {
            return $http.post('/api/projects', project).then(handleSuccess, handleError('Error creating project'));
        }

        function Delete(id) {
            return $http.delete('/api/projects/' + id).then(handleSuccess, handleError('Error deleting project'));
        }

        // private functions

        function handleSuccess(res) {
            return res.data;
        }

        function handleError(error) {
            return function () {
                return { success: false, message: error };
            };
        }
    }

})();
