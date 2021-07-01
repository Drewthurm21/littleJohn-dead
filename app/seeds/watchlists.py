from app.models import db, Portfolio

def seed_watchlists():

    watchlist = watchlist(
        name = "My 1st watchlist",
        user_id = 1
    )

    watchlist2 = watchlist(
        name = "My 1st watchlist",
        user_id = 2
    )

    db.session.add(watchlist)
    db.session.add(watchlist2)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_watchlists():
    db.session.execute('TRUNCATE watchlists RESTART IDENTITY CASCADE;')
    db.session.commit()
