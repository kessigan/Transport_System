import psycopg2
        
def mapUserTypeToTable(user_type):
	conn = psycopg2.connect(database="MainDB", user="postgres", password="password", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	senders = []
	if user_type == "sender":
		cur.execute("SELECT * FROM senders_table;")
		cur.execute("SELECT Name, Surname FROM senders_table")
		senders = cur.fetchall()
	elif user_type == "driver":
		cur.execute("SELECT * FROM drivers_table;")
		cur.execute("SELECT Name, Surname FROM drivers_table")
		senders = cur.fetchall()
	elif user_type == "receiver":
		cur.execute("SELECT * FROM receivers_table;")
		cur.execute("SELECT Name, Surname FROM receivers_table")
		senders = cur.fetchall()
		
	#remove the name and sentence aka first lines of the db
	senders = senders[1:]
	
	return senders
		
