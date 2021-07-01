from .db import db


class Portfolio(db.Model):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    balance = db.Column(db.Numeric(asdecimal=False), nullable=False)
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'balance': self.balance
        }

    owner = db.relationship('User', back_populates='portfolios')
    trade = db.relationship('Trade', back_populates='portfolio')