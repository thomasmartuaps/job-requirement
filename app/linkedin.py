import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, Response, session, url_for, jsonify, json
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('linkedin', __name__, url_prefix='/linkedin')

@bp.route('/', methods=('GET', 'POST'))
def get():
    if request.method == 'GET':
        newdict = {
            "spam": "egg",
            "foo": "bar"
        }
        response = Response(
            response=json.dumps(newdict),
            status=200,
            mimetype='application/json'
        )
        return response

@bp.route('/user', methods=('GET', 'POST'))
def user():
    response = Response(
        response=json.dumps({
            "user": "token"
        }),
        status=200,
        mimetype='application/json'
    )
    return response