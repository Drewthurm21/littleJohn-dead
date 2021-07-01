from .db import db


class Watchlist_stock(db.Model):
    __tablename__ = 'watchlist_stocks'

    id = db.Column(db.Integer, primary_key = True)
    watchlist_id = db.Column(db.Integer, db.ForeignKey('watchlists.id'), nullable = False)
    ticker = db.Column(db.String(10), nullable = False, unique = True)


    def to_dict(self):
        return {
            'id': self.id,
            'watchlist_id': self.watchlist_id,
            'ticker': self.ticker
        }


    watchlist = db.relationship('Watchlist', back_populates='stocks')