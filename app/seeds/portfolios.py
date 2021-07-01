# from werkzeug.security import generate_password_hash
from app.models import db, Portfolio

def seed_portfolios():

    portfolio = Portfolio(
        owner_id = 1,
        balance = 10000
    )

    db.session.add(portfolio)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_portfolios():
    db.session.execute('TRUNCATE portfolios RESTART IDENTITY CASCADE;')
    db.session.commit()
