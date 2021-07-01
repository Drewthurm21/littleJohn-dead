from .db import db
import datetime

class Trade(db.Model):
    __tablename__ = 'trades'


    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'), nullable=False)
    buy_sell = db.Column(db.String(10), nullable=False)
    ticker = db.Column(db.String(10), nullable= False)
    total_price = db.Column(db.Numeric(asdecimal=False), nullable=False)
    total_units = db.Column(db.Numeric(asdecimal=False), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())


    def to_dict(self):
        return {
            'id': self.id,
            'portfolio_id': self.portfolio_id,
            'buy_sell': self.buy_sell,
            'ticker': self.ticker,
            'total_price': self.order_total,
            'total_units': self.total_units,
            'timestamp': self.timestamp
        }


    portfolio = db.relationship('Portfolio', back_populates='trade')
