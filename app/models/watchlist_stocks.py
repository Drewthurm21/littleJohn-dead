from .db import db
from sqlalchemy.orm import relationship


class Watchlist_stock(db.Model):
    __tablename__ = 'watchlist_stocks'

    id = db.Column(db.Integer, primary_key = True)
    watchlist_id = db.Column(db.Integer, ForeignKey='watchlists', nullable = False)
    ticker = db.Column(db.String(10), nullable = False, unique = True)

    watchlist = relationship('Watchlist', back_populates='watchlist_stocks')