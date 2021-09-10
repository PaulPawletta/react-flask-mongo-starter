import os
from flask import Flask
from flask_restx import Api
from mongoengine import connect
from v1.resources.todos import todos
from dotenv import load_dotenv

from config import Development, Production

load_dotenv()

app = Flask(__name__)

if str.lower(os.environ['FLASK_ENV']) == 'production':
    app.config.from_object(Production())
    app.config['MONGODB_URL'] = os.environ['MONGODB_URL']
else:
    app.config.from_object(Development())

connect('app', host=app.config['MONGODB_URL'])

api = Api(app)
api.add_namespace(todos)

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])