from Config.Connect import *

class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = connect