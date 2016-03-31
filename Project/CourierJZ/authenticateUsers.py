import csv

def getListOfAllUsers():
	all_users = {}
	with open('login_details.csv', 'rb') as csvfile:
		loginreader = csv.reader(csvfile,delimiter=';')

		for row in loginreader:
			all_users[row[0]] = all_users[row[1]]

	return all_users



def checkIfUserIsInList(dict_of_all_users,user,password):
	return_val = False
	if user in dict_of_all_users:
		if password == dict_of_all_users[user]:
			return_val =  True
		else:
			return_val = False

	return return_val

def authenticateUser(user,password):
	dict_of_all_users = getListOfAllUsers()
	is_user = checkIfUserIsInList(dict_of_all_users,user,password)

	print is_user
	


		



