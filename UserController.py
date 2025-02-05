from Config import Connect
from Controllers import UniversalControllerDB
import pymysql
from Models.User import *


def login():
    cursor = UniversalControllerDB.connection.cursor(pymysql.cursors.DictCursor)

    while True:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")


        query = "SELECT * FROM users WHERE login = %s AND password = %s"
        cursor.execute(query, (login, password))
        user = cursor.fetchone()


        if user:

            try:

                role_id = user.get('role_id')
                if role_id == 1:
                    print(role_id)
                    print("Успешно for Admin")
                elif role_id == 2:
                    print("Успешно for User")
                else:
                    print("Успешно, но неизвестная роль")
            except KeyError:
                print("Ошибка: отсутствует ключ role_id в данных пользователя.")
            break
        else:
            choice = input("Неправильный логин или пароль. Попробуйте повторить? (y/n): ")
            if choice.lower() != 'y':
                break

    UniversalControllerDB.connection.close()

def register():
    cursor = UniversalControllerDB.connection.cursor(pymysql.cursors.DictCursor)

    while True:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        # Проверка, существует ли уже пользователь с таким логином
        query = "SELECT * FROM users WHERE login = %s"
        cursor.execute(query, (login,))
        user = cursor.fetchone()

        if user:
            print("Ошибка: Пользователь с таким логином уже существует.")
            choice = input("Попробовать снова? (y/n): ")
            if choice.lower() != 'y':
                break
        else:
            # Добавление нового пользователя
            try:
                # Вы можете установить значение по умолчанию для роли или запросить его у пользователя
                full_name = input("Введите ФИО: ")
                phone_num = input("Введите номер телефона: ")
                email = input("Введите mail(по желанию): ")
                insert_query = "INSERT INTO users (login, password, full_name, phone_num, email, role_id) VALUES (%s, %s, %s, %s, %s, 2)"
                cursor.execute(insert_query, (login, password, full_name, phone_num, email,))
                UniversalControllerDB.connection.commit()  # Сохранение изменений
                print("Регистрация прошла успешно!")
                break
            except ValueError:
                print("Ошибка: Неверное значение. Попробуйте снова.")
            except Exception as e:
                print(f"Произошла ошибка: {e}")
                UniversalControllerDB.connection.rollback()  # Отмена изменений в случае ошибки

    UniversalControllerDB.connection.close()

#Изменение заявки
def ApplicationChangeStatus(id, status):
    cursor = UniversalControllerDB.connection.cursor()

    cursor.execute(f"UPDATE applications SET status = {status} WHERE id = {id}")

    UniversalControllerDB.connection.commit()
    if status == 1:
        print("Заявление изменено на |ОДОБРЕНО|")
    if status == 2:
        print("Заявление изменено на |ОТКЛОНЕНО|")

def userID(name):
    return Users.get(Users.login == name).id



if __name__ == "__main__":
    login()


