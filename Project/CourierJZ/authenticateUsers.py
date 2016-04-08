import csv
import readDatabase
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

def getListOfAllUsers(user_type):
	all_users = []
	all_users = readDatabase.mapUserTypeToTable(user_type)
	
	return all_users

def checkIfUserIsInList(list_of_all_users,user,password,user_type):
	return_val = False
	designation = "unknown"
	
	for user_data in list_of_all_users:
		print "THE DATA CHECK"
		print convert(user_data[0])
		print convert(user_data[1])
		if user == convert(user_data[0]):
			if password == convert(user_data[1]):
				return_val =  True
				designation = user_type
				break
		else:
			return_val = False
				
	return return_val,designation
			

def authenticateUser(user,password,user_type):
	dict_of_all_users = getListOfAllUsers(user_type)

	is_user, designation = checkIfUserIsInList(dict_of_all_users,user,password,user_type)
	
	if is_user == True:
		is_user1 = "allow"
	else:
		is_user1 = "deny"
				
	return is_user1, designation
	
def writeVerdictToCSVFile(is_true):
	with open('allow_login.csv', 'wb') as csvfile:
		loginwriter = csv.writer(csvfile)
		
		loginwriter.writerow([is_true])
	
def readVerdictFromCSVFile():
	verdict = ""
	with open('allow_login.csv', 'rb') as csvfile:
		loginreader = csv.reader(csvfile)
		
		for row in loginreader:
			verdict = row		
	return verdict
	


		



