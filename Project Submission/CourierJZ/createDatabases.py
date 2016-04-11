import psycopg2


def createMainDatabase():
	conn = psycopg2.connect(database="MainDB", user="postgres", password="password", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	createDriverTable(cur)
	createSenderTable(cur)
	createReceiverTable(cur)
	createDispatcherTable(cur)
	
	createPackagesPickupTable(cur)
	createPackagesStorageTable(cur)
	
	conn.commit()
	conn.close()
	
	
def createDriverTable(cur):
	cur.execute("DROP TABLE IF EXISTS drivers_table")
	cur.execute("CREATE TABLE drivers_table (id serial PRIMARY KEY, Name varchar, Surname varchar, Address varchar, City varchar, PostCode varchar, Email varchar, Phone varchar, Password varchar, WorkStatus varchar);")
	
	f = open(r'drivers.csv', 'r')
	cur.copy_from(f, "drivers_table", sep=';')
	f.close()
	
	print "Opened database successfully"
	
def createSenderTable(cur):
	cur.execute("DROP TABLE IF EXISTS senders_table")
	cur.execute("CREATE TABLE senders_table (id serial PRIMARY KEY, Name varchar, Surname varchar, Address varchar, City varchar, PostCode varchar, Email varchar, Phone varchar, Password varchar);")
	
	f = open(r'senders.csv', 'r')
	cur.copy_from(f, "senders_table", sep=';')
	f.close()
	
	print "Opened database successfully"
	
def createReceiverTable(cur):
	cur.execute("DROP TABLE IF EXISTS receivers_table")
	cur.execute("CREATE TABLE receivers_table (id serial PRIMARY KEY, Name varchar, Surname varchar, Address varchar, City varchar, PostCode varchar, Email varchar, Phone varchar, Password varchar);")
	
	f = open(r'receivers.csv', 'r')
	cur.copy_from(f, "receivers_table", sep=';')
	f.close()
	
	print "Opened database successfully"

def createDispatcherTable(cur):
	cur.execute("DROP TABLE IF EXISTS dispatchers_table")
	cur.execute("CREATE TABLE dispatchers_table (id serial PRIMARY KEY, Name varchar, Surname varchar, Address varchar, City varchar, PostCode varchar, Email varchar, Phone varchar, Password varchar);")
	
	f = open(r'dispatcher.csv', 'r')
	cur.copy_from(f, "dispatchers_table", sep=';')
	f.close()
	
	print "Opened database successfully"
	
def createPackagesPickupTable(cur):
	cur.execute("DROP TABLE IF EXISTS packages_pickup_table")
	cur.execute("CREATE TABLE packages_pickup_table (id serial PRIMARY KEY, Weight varchar, Destination varchar);")
	
	f = open(r'packages_pickup.csv', 'r')
	cur.copy_from(f, "packages_pickup_table", sep=';')
	f.close()
	
	print "Opened database successfully"
	
def createPackagesStorageTable(cur):
	cur.execute("DROP TABLE IF EXISTS packages_storage_table")
	cur.execute("CREATE TABLE packages_storage_table (id serial PRIMARY KEY, Weight varchar, Destination varchar);")
	
	f = open(r'packages_storage.csv', 'r')
	cur.copy_from(f, "packages_storage_table", sep=';')
	f.close()
	
	print "Opened database successfully"
	
createMainDatabase()

