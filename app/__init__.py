import os

from flask import Flask

from flask import (
    request, json
)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # import blueprint(s)

    from . import linkedin

    app.register_blueprint(linkedin.bp)


    # routes
    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route('/jobs', methods=('GET', 'POST'))
    def jobs():
        if request.method == 'GET':
            newdict = {
                "jobs": "list",
                "spam": "egg"
            }
            response = app.response_class(
                response=json.dumps(newdict),
                status=200,
                mimetype='application/json'
            )
            return response

    return app