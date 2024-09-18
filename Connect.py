from peewee import *

connect = MySQLDatabase(
    'narusheniynet',  # Required by Peewee.
    user='root',  # Will be passed directly to psycopg2.
    password='Svor228811',  # Ditto.
    host='localhost')  # Ditto.)