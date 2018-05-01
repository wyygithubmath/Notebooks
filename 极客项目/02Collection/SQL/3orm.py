#! /usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------
# author wyy
# date 20170406
# -----------------------

from sqlpackages import *

engine = create_engine("sqlite:///:memory:", echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

Base.metadata.create_all(engine)


ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')

print(ed_user.name)


# session
Session = sessionmaker(bind=engine)
# Session = sessionmaker()
# Session.configure(bind=engine)

session = Session()

session.add(ed_user)
our_user = session.query(User).filter_by(name='ed').first()


session.add_all([
    User(name='wendy', fullname='Wendy Williams', password='foobar'),
    User(name='mary', fullname='Mary Contrary', password='xxg527'),
    User(name='fred', fullname='Fred Flinstone', password='blah')])
session.commit()

# querying
for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)

for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)

for row in session.query(User, User.name).all():
    print(row.User, row.name)

# # filter