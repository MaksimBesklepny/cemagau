from Models.Applications import *

class AplicationController():
    # Вывод всех записей
    def show(self):
        return Aplications.select()

#     создать запись
    def create(self, input_discription,input_status,input_number_auto,input_user_id):
        Applications.create(description = input_discription,
                           status = input_status,
                           car_num = input_number_auto,
                           user_id = input_user_id)
        return True
#     вывод записи одного пользователя
    def show_one(self,us_id):
        return Aplications.select().where(Aplications.user_id == us_id)

    def update_status(self,discription_id, new_status):
        Aplications.update({Aplications.status: new_status}).where(Aplications.id == discription_id).execute()

    def delete(self,discription_id):
        Aplications.delete().where(Aplications.id == discription_id).execute()

if __name__ == "__main__":
    app = AplicationController()