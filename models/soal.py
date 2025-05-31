from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Soal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pertanyaan = db.Column(db.Text, nullable=False)
    jawaban = db.Column(db.String(100), nullable=False)
    tingkat = db.Column(db.String(20), nullable=False)
