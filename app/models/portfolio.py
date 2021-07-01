from .db import db


class Portfolio(db.Model):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'), nullable=False)
    balance = db.Column(db.Numeric(asdecimal=False), nullable=False)
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'balance': self.balance
        }

    owner = db.relationship('User', back_populates='portfolios')
    trade = db.relationship('Portfolio', back_populates='portfolio')