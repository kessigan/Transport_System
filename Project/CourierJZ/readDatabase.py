import psycopg2
import collections
        
def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data
        
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
	elif user_type == "dispatcher":
		cur.execute("SELECT * FROM dispatchers_table;")
		cur.execute("SELECT Name, Surname FROM dispatchers_table")
		senders = cur.fetchall()
		
	#remove the name and sentence aka first lines of the db
	senders = senders[1:]
	
	return senders
	
def readThePackages():
	conn = psycopg2.connect(database="MainDB", user="postgres", password="password", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	packages_pickup = []
	packages_storage = []
	
	cur.execute("SELECT * FROM packages_pickup_table;")
	packages_pickup = cur.fetchall()
	cur.execute("SELECT * FROM packages_storage_table;")
	packages_storage = cur.fetchall()
	
	#remove the name and sentence aka first lines of the db and change from unicode back to normal strings
	packages_pickup = convert(packages_pickup[1:])
	packages_storage = convert(packages_storage[1:])
	
	#convert the tuples to list
	packages_pickup = convertTupleToList(packages_pickup)
	packages_storage = convertTupleToList(packages_storage)
	
	return packages_pickup, packages_storage
	
def convertTupleToList(list_to_convert):
	converted_tuples_list = []
	tup_new = []
	for tup in list_to_convert:
		tup_new = list(tup)
		converted_tuples_list.append(tup_new)

	return converted_tuples_list
		
