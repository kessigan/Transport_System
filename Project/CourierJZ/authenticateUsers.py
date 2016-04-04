import csv

def getListOfAllUsers():
	all_users = []
	with open('login_details.csv', 'rb') as csvfile:
		loginreader = csv.reader(csvfile,delimiter=';')
		
		#skip the first row because those are the headings
		counter = 0
		for row in loginreader:
			if counter > 0: 
				all_users.append(row)	
			counter = counter + 1

	return all_users



def checkIfUserIsInList(list_of_all_users,user,password):
	return_val = False
	designation = "unknown"
	for user_data in list_of_all_users:
		if user == user_data[0]:
			if password == user_data[1]:
				return_val =  True
				designation = user_data[2]
				break
		else:
			return_val = False

	return return_val,designation

def authenticateUser(user,password):
	dict_of_all_users = getListOfAllUsers()
	is_user, designation = checkIfUserIsInList(dict_of_all_users,user,password)

	return is_user, designation
	


		



