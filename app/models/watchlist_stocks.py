from .db import db
from sqlalchemy.orm import relationship


class Watchlist_stock(db.Model):
    __tablename__ = 'watchlist_stocks'

    id = db.Column(db.Integer, primary_key = True)
    watchlist_id = db.Column(db.Integer, ForeignKey='watchlists', nullable = False)
    ticker = db.Column(db.String(10), nullable = False, unique = True)

    def to_dict(self):
        return {
            'id': self.id,
            'watchlist_id': self.watchlist_id,
            'ticker': self.ticker
        }

    watchlist = relationship('Watchlist', back_populates='watchlist_stocks')