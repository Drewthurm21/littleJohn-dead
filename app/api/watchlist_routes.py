from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Watchlist, Watchlist_stock

watchlist_routes = Blueprint('watchlists', __name__)


@watchlist_routes.route('')
def get_watchlists():
    watchlists = Watchlist.query.all()
    watchlists_list = [watchlist.to_dict() for watchlist in watchlists]
    return {'watchlists': watchlists_list}