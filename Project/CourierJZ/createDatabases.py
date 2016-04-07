import psycopg2


def createMainDatabase():
	conn = psycopg2.connect(database="MainDB", user="postgres", password="password", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	createDriverTable(cur)
	createSenderTable(cur)
	createReceiverTable(cur)
	
	conn.commit()
	conn.close()
	
	
def createDriverTable(cur):
	cur.execute("DROP TABLE IF EXISTS drivers_table")
	cur.execute("CREATE TABLE drivers_table (Name varchar, Surname varchar, Address varchar, City varchar, PostCode varchar, Email varchar, Phone varchar, Password varchar);")
	
	f = open(r'drivers.csv', 'r')
	cur.copy_from(f, "drivers_table", sep=';')
	f.close()
	
	print "Opened database successfully"
	
def createSenderTable(cur):
	cur.execute("DROP TABLE IF EXISTS senders_table")
	cur.execute("CREATE TABLE senders_table (Name varchar, Surname varchar, Address varchar, City varchar, PostCode varchar, Email varchar, Phone varchar, Password varchar);")
	
	f = open(r'senders.csv', 'r')
	cur.copy_from(f, "senders_table", sep=';')
	f.close()
	
	print "Opened database successfully"
	
def createReceiverTable(cur):
	cur.execute("DROP TABLE IF EXISTS receivers_table")
	cur.execute("CREATE TABLE receivers_table (Name varchar, Surname varchar, Address varchar, City varchar, PostCode varchar, Email varchar, Phone varchar, Password varchar);")
	
	f = open(r'receivers.csv', 'r')
	cur.copy_from(f, "receivers_table", sep=';')
	f.close()
	
	print "Opened database successfully"

createMainDatabase()

