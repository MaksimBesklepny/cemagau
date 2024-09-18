from Models.Base import *
class Roles(BaseModel):
    id = PrimaryKeyField()
    role = CharField()