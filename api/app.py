import os
from flask import Flask, Blueprint
from flask_restx import Api
from mongoengine import connect
from v1.resources.todos import todos
from dotenv import load_dotenv

from config import Development, Production

load_dotenv()

app = Flask(__name__)

# Blueprint to change URL base path to /api
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)
app.register_blueprint(blueprint)

if str.lower(os.environ['FLASK_ENV']) == 'production':
    app.config.from_object(Production())
    app.config['MONGODB_URL'] = os.environ['MONGODB_URL']
else:
    app.config.from_object(Development())

connect('app', host=app.config['MONGODB_URL'])

api.add_namespace(todos)

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])