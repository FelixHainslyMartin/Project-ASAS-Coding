import os

class Config:
    SECRET_KEY = 'rahasia'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///soal.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
