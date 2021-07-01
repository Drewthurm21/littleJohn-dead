from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Portfolio, Watchlist

user_routes = Blueprint('users', __name__)


@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/<int:id>/portfolios')
def user_portfolio(id):
    portfolios = Portfolio.query.filter_by(owner_id=id)
    portfolio_list = [portfolio.to_dict() for portfolio in portfolios]
    return {"portfolios": portfolio_list}


@user_routes.route('/<int:id>/watchlists')
def user_watchlists():
    watchlists = Watchlist.query.filter_by(user_id=id)
    watchlist_list = [watchlist.to_dict() for watchlist in watchlists]
    return {"watchlists": watchlist_list}