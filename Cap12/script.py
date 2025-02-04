import sqlite3

conn = sqlite3.connect('cap12_dsa.db')
cursor = conn.cursor()

sql_query = ('SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa')

cursor.execute(sql_query)

print(cursor.fetchall())

conn.commit()
cursor.close()
conn.close()