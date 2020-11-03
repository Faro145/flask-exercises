from app import db, Orders, Customers, Products

db.create_all()

ross = Customers(name='Ross', email='ross@mail.com')

watch =

db.session.add(ross)
db.session.add(watch)
db.session.commit()
