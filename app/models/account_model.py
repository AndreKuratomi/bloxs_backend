from dataclasses import dataclass

from app.configs.database import db
from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class Accountmodel(db.Model):
    idAccount: int
    idPerson: int
    balance: str
    dailyBalanceLimit: str
    flagActive: bool
    accountType: int
    creationDate: str

    __tablename__ = "accounts"

    idAccount = db.Column(db.Integer(11), primary_key=True)
    idPerson = db.Column(db.Integer(11))
    balance = db.Column(db.String(20))
    dailyBalanceLimit = db.Column(db.String(20))
    flagActive = db.Column(db.Boolean, default=False)
    accountType = db.Column(db.Integer, nullable=False)
    creationDate = db.Column(db.DateTime(), nullable=False, unique=True)
