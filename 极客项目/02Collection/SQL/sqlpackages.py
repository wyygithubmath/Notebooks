#! /usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------
# author wyy
# date 20170406
# -----------------------


# ORM
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy import Sequence
from sqlalchemy import ForeignKey

#core
from sqlalchemy.sql import select
from sqlalchemy.sql import and_, or_, not_

# session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


DNS = {
    "sqlite": "sqlite:///:memory:",
    "sqlite3": "sqlite:///D://Data//sql.db",
    "mysql": "mysql+pymysql://root:abcd1234@localhost"
}

def main():
    print("This is used to import basic informations !")

if __name__ == '__main__':
    main()
