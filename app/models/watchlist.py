from .db import db
from sqlalchemy.orm import relationship

class Watchlist(db.Model):
    __tablename__ = 'watchlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey='users', nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id
        }

    user = relationship('User', back_populates='watchlists')
    stocks = relationship('Watchlist_stock', back_populates='watchlists')