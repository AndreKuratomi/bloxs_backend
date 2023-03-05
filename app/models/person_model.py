from app.configs.database import db

from dataclasses import dataclass
# from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class PersonModel(db.Model):
    idPerson: int
    name: str
    cpf: str
    birthday: str

    __tablename__ = "person"

    idPerson = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(50))
    cpf = db.Column(db.String(11), unique=True)
    birthday = db.Column(db.String(10), nullable=False)
