#! /usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------
# author wyy
# date 20170411
# -----------------------



from sqlpackages import *


conn = create_engine("sqlite:///:memory:", echo=True)


conn.execute(
    '''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')
# Insert
ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)
conn.execute(ins, 'bear', 2, 1000)
conn.execute(ins, 'weasel', 1, 2000)
# Query
rows = conn.execute('SELECT * FROM zoo')
for row in rows:
    print(row)



