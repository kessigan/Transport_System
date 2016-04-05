import psycopg2


def createDriverDatabase():
	conn = psycopg2.connect(database="DriverDB", user="postgres", password="password", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	cur.execute("DROP TABLE IF EXISTS drivers_table")
	cur.execute("CREATE TABLE drivers_table (Name varchar, Surname varchar, Address varchar, City varchar, PostCode varchar, Email varchar, Phone varchar, Password varchar);")
	
	f = open(r'drivers.csv', 'r')
	cur.copy_from(f, "drivers_table", sep=';')
	f.close()
	
	print "Opened database successfully"
	
	conn.commit()
	conn.close()
	
def createSenderDatabase():
	conn = psycopg2.connect(database="SenderDB", user="postgres", password="password", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	cur.execute("DROP TABLE IF EXISTS senders_table")
	cur.execute("CREATE TABLE senders_table (Name varchar, Surname varchar, Address varchar, City varchar, PostCode varchar, Email varchar, Phone varchar, Password varchar);")
	
	f = open(r'senders.csv', 'r')
	cur.copy_from(f, "senders_table", sep=';')
	f.close()
	
	print "Opened database successfully"
	
	conn.commit()
	conn.close()
	
def createReceiverDatabase():
	conn = psycopg2.connect(database="ReceiverDB", user="postgres", password="password", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	cur.execute("DROP TABLE IF EXISTS receivers_table")
	cur.execute("CREATE TABLE receivers_table (Name varchar, Surname varchar, Address varchar, City varchar, PostCode varchar, Email varchar, Phone varchar, Password varchar);")
	
	f = open(r'receivers.csv', 'r')
	cur.copy_from(f, "receivers_table", sep=';')
	f.close()
	
	print "Opened database successfully"
	
	conn.commit()
	conn.close()

createDriverDatabase()
createSenderDatabase()
createReceiverDatabase()
