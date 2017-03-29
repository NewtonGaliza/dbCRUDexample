import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'root', 'users')

with con:

	cur = con.cursor()
	
	'''
	first time only
	try:
		cur.execute('CREATE TABLE User(Id INT PRIMARY KEY AUTO_INCREMENT, Login VARCHAR(25), Passwd VARCHAR(25),FirstName VARCHAR(25), LastName VARCHAR(25))')
		con.commit()
	except:
		con.rollback()

	print ('Table Created')
	'''
	
def add(login, passwd, firstName, lastName):
	sql = '''
		INSERT INTO User (Login, Passwd, FirstName, LastName)
		VALUES ('%s', '%s', '%s', '%s')
	''' % (login, passwd, firstName, lastName)

	try:
		cur.execute(sql)
		con.commit()
	except Error as error:
		print(error)
        con.rollback()
	con.close()
	print ('User OK')

def list():
	try:
		cur.execute('SELECT * FROM User')
		for i in xrange(cur.rowcount):
			row = cur.fetchone()
			print ('Id-'+str(row[0])+' Login-'+str(row[1])+' First Name-'+str(row[3])+' Last Name-'+row[4])		
	except Error as error:
		print(error)
        con.rollback()
	con.close()

def updateLogin(login, usId):
	login = "'"+login+"'"
	sql = "UPDATE User SET Login = %s WHERE Id = %s" % (login,usId)
	try:
		cur.execute(sql)
		con.commit()
	except Error as error:
		print(error)
        con.rollback()
	con.close()

def updatePasswd(passwd, usId):
	passwd = "'"+passwd+"'"
	sql = "UPDATE User SET Passwd = %s WHERE Id = %s" % (passwd,usId)
	try:
		cur.execute(sql)
		con.commit()
	except Error as error:
		print(error)
        con.rollback()
	con.close()

def updateFistName(firstName, usId):
	firstName = "'"+firstName+"'"
	sql = "UPDATE User SET FirstName = %s WHERE Id = %s" % (firstName, usId)
	try:
		cur.execute(sql)
		con.commit()
	except Error as error:
		print(error)
        con.rollback()
	con.close()

def updateLastName(lastName, usId):
	lastName = "'"+lastName+"'"
	sql = "UPDATE User SET LastName = %s WHERE Id = %s" % (lastName, usId)
	try:
		cur.execute(sql)
		con.commit()
	except Error as error:
		print(error)
        con.rollback()
	con.close()

def delete(usId):
	sql = 'DELETE FROM User WHERE Id = %s' % usId
	try:
		cur.execute(sql)
		con.commit()
	except Error as error:
		print(error)
        con.rollback()
	con.close()

print('###MENU####\nPress 1 to ADD user\nPress 2 to LIST all users\nPress 3 to UPDATE user\nPress 4 to DELETE user')
op = input('Option:')

if op == 1:
	login = raw_input('Login:')
	passwd = raw_input('Password:')
	firstName = raw_input('First name:')
	lastName = raw_input('Last Name:')
	add(login, passwd, firstName, lastName)

elif op == 2:
	list()

elif op == 3:
	usId = raw_input('Select Id of User to change:')
	print('##MENU-UPDATE##\nPress 1 to update Login\nPress 2 to update Password\nPress 3 to update First Name\nPress 4 to update Last Name')
	op2 = input('Option:')
	if op2 == 1:
		login = raw_input('Enter new Login:')
		updateLogin(login, usId)
	elif op2 == 2:
		passwd = raw_input('Enter new Password:')
		updatePasswd(passwd, usId)
	elif op2 == 3:
		firstName = raw_input('Enter new First Name:')
		updateFistName(firstName, usId)
	elif op2 == 4:
		lastName = raw_input('Enter new Last Name:')
		updateLastName(lastName, usId)
	else:
		print('Invalid Option')

elif op == 4:
	usId = raw_input('Select Id of User to DELETE:')
	print('Deleted')
	delete(usId)

else:
	print('Invalid Option')
