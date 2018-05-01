#! /usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------
# author wyy
# date 20170406
# -----------------------


from sqlpackages import *

engine = create_engine("sqlite:///:memory:", echo=True)

metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
)

addresses = Table('addresses', metadata,
  Column('id', Integer, primary_key=True),
  Column('user_id', None, ForeignKey('users.id')),
  Column('email_address', String, nullable=False)
)

metadata.create_all(engine)

ins = users.insert().values(name='jack', fullname='Jack Jones')

conn = engine.connect()
res = conn.execute(ins)


