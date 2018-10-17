'use strict'

angular.module('app')
  .factory 'config', ['$http', '$log', ($http, $log) ->
    @config = {}

    success = (response) =>
      $log.debug 'Configuration loaded.'
      @config = response

    fail = (response) ->
      $log.error 'Could not load configuration!'

    # TODO Use a build tool to generate config.js?
    $http.get('/config.json', {async: false, cache: true})
      .then(success, fail)

    get: =>
      @config
  ]
