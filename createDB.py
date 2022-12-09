import sqlite3

con = sqlite3.connect('imc.db')
cur = con.cursor()

#Criar a tabela
sql = 'create table imc'\
      '(id integer primary key'\
      'nome varchar(100)'\
      'altura int(32),'\
      'peso int(32),'\
      'total int(64))'
cur.execute(sql)

con.close()