from Models.Base import *
from Models.User import *
class Applications(BaseModel):
    id = PrimaryKeyField()
    description = TextField()
    status = BooleanField()
    car_num = CharField()
    user_id = ForeignKeyField(Users)