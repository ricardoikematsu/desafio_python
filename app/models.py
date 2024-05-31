from datetime import datetime
from app import db

class DadosTempo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cidade = db.Column(db.String(100), nullable=False)
    dados = db.Column(db.JSON, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return DadosTempo.query.all()