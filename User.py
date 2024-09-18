from Models.Base import *
from Models.Role import *
class Users(BaseModel):
    id = PrimaryKeyField()
    login = CharField()
    password = CharField()
    full_name = CharField()
    email = CharField()
    phone_num = IntegerField()
    role_id = ForeignKeyField(Roles)