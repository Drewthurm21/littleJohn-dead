from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Portfolio

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