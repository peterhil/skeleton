'use strict'

angular.module('app')
  .factory('errorInterceptor', ['$q', '$log', 'growl', ($q, $log, growl) ->
    response: (response) ->
      $log.debug "success with status #{response.status}"
      response || $q.when response

    responseError: (rejection) ->
      $log.error "error with status #{rejection.status} and data: #{rejection.data['message']}"

      switch rejection.status
        when 403
          growl.error "You don't have the right to do this"
        when 404
          growl.error "Not found"
        when 0
          growl.error "No connection, internet is down?"
        else
          growl.error "#{rejection.data['message']}"

      # do something on error
      $q.reject rejection
  ])
