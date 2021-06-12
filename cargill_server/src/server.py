import os
from flask import Flask, request, jsonify, Response, send_from_directory
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

dir_path = os.path.dirname(__file__)

cargill_app = Flask(__name__)
cors = CORS(cargill_app)
cargill_app.config['CORS_HEADERS'] = 'Content-Type'

SWAGGER_URL = '/api/docs'
API_URL = '/docs/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={
        'app_name': "Cargill Team API Project",
    }
)

cargill_app.config.from_object('config.DevConfig')
db = SQLAlchemy(cargill_app)

"""
Database schema
"""


class TeamDetails(db.Model):
    __tablename__ = "TeamDetails"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), default='', nullable=False)
    role = db.Column(db.String(128), default='', nullable=False)

    def __init__(self, name, role):
        self.name = name
        self.role = role


db.create_all()
db.session.commit()


@cargill_app.route("/docs/swagger.json")
def specs():
    print(os.getcwd())
    return send_from_directory(dir_path, "swagger.json")


"""
APIs
"""


@cargill_app.route('/', methods=['GET'])
@cross_origin()
def home():
    """ This method is a default landing for any request acting as a home url """
    return jsonify({
        'message': 'Welcome to this flask application for db interaction'
    })


@cargill_app.route('/add_team', methods=['POST'])
@cross_origin()
def add_team():
    """ This method is a POST endpoint which take
      team_name and team_role
      add the above to the table TeamDetails
     :returns Success once the db operation is completed
     """
    data = request.json
    print('Data received -> ', data)
    try:
        post = TeamDetails(data['team_name'], data['team_role'])
        db.session.add(post)
        db.session.commit()
        posts = TeamDetails.query.all()
        print('posts -> ', posts)
        resp = Response('{"message": "success"}', status=200, mimetype='application/json')
    except Exception as error:
        resp = Response('{"message": "failure", "error": "{0}"}'.format(error), status=503, mimetype='application/json')
    return resp


@cargill_app.route('/get_team/<team_name>', methods=['GET'])
@cross_origin()
def get_team(team_name):
    """ This method is a GET endpoint which take
      :param team_name
      query the table TeamDetails and
     :returns list of roles under the team
     """
    try:
        roles = TeamDetails.query.filter_by(name=team_name).all()
        response = set([role.__dict__['role'] for role in roles])
        print('Roles -> ', response)
        resp = jsonify(list(response))
    except Exception as error:
        resp = Response('{"message": "failure", "error": "{0}"}'.format(error), status=503, mimetype='application/json')
    return resp


if __name__ == '__main__':
    db.init_app(cargill_app)
    cargill_app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    cargill_app.run()
