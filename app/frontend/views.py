#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import current_app, Blueprint, render_template
from flask import jsonify, url_for, send_from_directory

from app.helpers import route
from ..deco import templated


bp = Blueprint('front', __name__)


@route(bp, '/config.json')
def config():
    """
    Expose some of the application config into the front end.

    Documentation about config values:
    http://flask.pocoo.org/docs/config/#configuring-from-files
    """
    exposed_config = [
        'APP_NAME',
        'ASSETS_DEBUG',
        'DEBUG',
        'PREFERRED_URL_SCHEME',
        'SERVER_NAME',
        'TESTING',
        'API_URL',
        'API_SERVER',
    ]
    return jsonify(dict([
        (k.lower(), v) for k, v in current_app.config.iteritems() if k in exposed_config
    ]))

# See http://flask-restful.readthedocs.org/en/latest/ or https://github.com/ametaireau/flask-rest/
# on how to properly implement an REST API with Flask
@route(bp, '/api/<entity>')
def api(entity):
    return jsonify({entity: [
        {'url': '/one'},
        {'url': '/two'},
    ]})

@route(bp, '/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(bp.root_path, 'static'),
        'favicon.ico', mimetype='image/vnd.microsoft.icon'
    )

@route(bp, '/')
def index():
    """Returns the index."""
    return render_template('index.html')

@route(bp, '/one')
@templated('/one.html')
def one():
    return dict(greeting='hello')

@route(bp, '/one/<greeting>')
def one_with_greeting(greeting='hello'):
    return render_template('/one.html', greeting=greeting)

@route(bp, '/two')
@templated('/two.html')
def two():
    return dict()
