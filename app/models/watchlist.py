from .db import db
from sqlalchemy.orm import relationship

class Watchlist(db.Model):
    __tablename__ = 'watchlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey='users', nullable=False)

    user = relationship('User', back_populates='watchlists')