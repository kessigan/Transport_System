import psycopg2

conn = psycopg2.connect(database="initialDb", user="postgres", password="password", host="127.0.0.1", port="5432")

print "Opened database successfully"

