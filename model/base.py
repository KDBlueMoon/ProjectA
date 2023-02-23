from peewee import Model, BooleanField
from sql_app.database import db


class BaseModel(Model):
    
    class Meta:
        database = db