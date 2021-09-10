import json
from flask import abort, request
from flask_restx import Namespace, Resource, fields
from v1.database.models import Todo
from mongoengine import DoesNotExist

todos = Namespace('v1/todos', description='Todos namespace')

resource_fields = todos.model('Resource', {
    'title': fields.String,
    'content': fields.String,
})

@todos.route('/')
class TodosApi(Resource):
    def get(self):
        '''List all Todos'''
        todos = Todo.objects.all()
        return json.loads(todos.to_json()), 200
    
    @todos.expect(resource_fields)
    def post(self):
        '''Create a new Todo'''
        body = request.get_json()
        todo = Todo(**body).save()
        id = todo.id
        return {'id': str(id)}, 201


@todos.route('/<id>')
@todos.response(404, 'Todo not found')
@todos.param('id', 'The task identifier')
class TodoApi(Resource):
    def get(self, id):
        '''Fetch a given Todo'''
        try:
            todo = Todo.objects.get(id=id)
            return json.loads(todo.to_json()), 200
        except(DoesNotExist):
            abort(404)
        except:
            abort(500)
