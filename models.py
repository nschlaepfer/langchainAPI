from datetime import datetime
from peewee import Model, CharField, DateTimeField, TextField, SqliteDatabase

# Assuming the use of Peewee ORM for simplicity and SQLite as the database
db = SqliteDatabase('langchain_docs.db')

class BaseModel(Model):
    """
    Base model class that specifies the database.
    """
    class Meta:
        database = db

class Document(BaseModel):
    """
    Model representing a document fetched from the Langchain documentation.
    """
    url = CharField(unique=True)
    title = CharField()
    content = TextField()
    fetched_at = DateTimeField(default=datetime.now)

    class Meta:
        table_name = 'documents'

def initialize_db():
    """
    Initializes the database by creating tables.
    """
    with db:
        db.create_tables([Document])

# Example usage
if __name__ == '__main__':
    initialize_db()
