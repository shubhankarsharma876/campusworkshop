"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaacke7avj5o48l6dmg-a",
        database="postgresql_eqxe",
        user="postgresql_eqxe_user",
        password="MmhPkzKnyutyWbkf0xZgYmYAQjcfrfIk")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
