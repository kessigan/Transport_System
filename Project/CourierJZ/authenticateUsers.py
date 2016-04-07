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
	


		



