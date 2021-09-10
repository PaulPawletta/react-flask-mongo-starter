from mongoengine import DynamicDocument, StringField

class Todo(DynamicDocument):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)