# -*- coding: utf-8 -*-
import sqlite3

connect = sqlite3.connect("db_shop")

cursor = connect.cursor()

# cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")

cursor.close()

connect.commit()

connect.close()
