import psycopg2

conn = psycopg2.connect(database="DriverDB", user="postgres", password="password", host="127.0.0.1", port="5432")
cur = conn.cursor()

cur.execute("CREATE TABLE drivers_table (id serial PRIMARY KEY, name varchar, surname varchar, address varchar, city varchar, post varchar, code varchar, email varchar, phone varchar, password varchar);")

f = open(r'drivers.csv', 'r')
cur.copy_from(f, drivers_table, sep=';')
f.close()

print "Opened database successfully"

conn.commit()
conn.close()

