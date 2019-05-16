from InfrastructureLayer.userDAO import UserDao

class User:
	def __init__(self, data=None):
		self.user = {}

		if data:
			self.user['user_id'] = data['user_id']
			self.user['username'] = data['username']
			self.user['password'] = data['password']
			self.user['first_name'] = data['first_name']
			self.user['last_name'] = data['last_name']
			self.user['phone'] = data['phone']
			self.user['admin'] = data['admin']

	def factory(self, username, password, first_name, last_name, phone, admin):
		dao = UserDao()

		user_id = dao.register(username, password, first_name, last_name, phone, admin)
		data = dao.getUserById(user_id)

		self.user['user_id'] = data['user_id']
		self.user['username'] = data['username']
		self.user['password'] = data['password']
		self.user['first_name'] = data['first_name']
		self.user['last_name'] = data['last_name']
		self.user['phone'] = data['phone']
		self.user['admin'] = data['admin']

	def getInfo(self):
		return self.user

class UserRepository:
	def __init__(self):
		self.dao = UserDao()

	def getAllUsers(self):
		result = self.dao.getAllUsers()
		users = []

		for row in result:
			user = User(row)
			users.append(user)

		return users

	def getUserById(self, user_id):
		pass

	def getUserByUsername(self, username):
		result = self.dao.getUserByUsername(username)
		user = None

		if result:
			user = User(result)

		return user