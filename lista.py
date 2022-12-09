# -*- coding: utf8 -*-
import sqlite3

con = sqlite3.connect('imc.db')
cur = con.cursor()

cur.execute('select * from imc')

recset = cur.fetchall()

for rec in recset:
    print ('%d: %s, %d, %d, %d' % rec)

con.close()

