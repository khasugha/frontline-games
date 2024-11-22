# config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
    "mssql+pyodbc://@localhost\\SQLEXPRESS/FrontlineGames?"
    "driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
)
