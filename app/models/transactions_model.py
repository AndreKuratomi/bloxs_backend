from app.configs.database import db

from dataclasses import dataclass
# from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class TransactionsModel(db.Model):
    idTransaction: int
    idAccount: int
    value: str
    transactionDate: str

    __tablename__ = 'transactions'

    idTransaction = db.Column(db.Integer, primary_key=True)
    idAccount = db.Column(db.Integer) # 1 -> M
    value = db.Column(db.String(20))
    transaction_date = db.Column(db.DateTime(), nullable=False, unique=True)
