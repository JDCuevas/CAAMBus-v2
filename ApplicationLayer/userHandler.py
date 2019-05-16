from flask import jsonify
from DomainLayer.user import User, UserRepository
from DomainLayer.driver import Driver

class UserHandler:
	# Schema: user_id, username, password, first_name, last_name, phone, admin
	repo = UserRepository()

	def register(self, username, password, first_name, last_name, phone, admin, license):
		user = User()
		user.factory(username, password, first_name, last_name, phone, admin)
		print(user.user)
		if admin != 'True':
			driver = Driver().factory(license, user.user['user_id'])

		return user

	def getAllUsers(self):
		result = self.repo.getAllUsers()
		users = []

		if result:
			for row in result:
				userInfo = row.getInfo()
				users.append(userInfo)

		return users

	def getUserByUsername(self, username):
		result = self.repo.getUserByUsername(username)
		user = None

		if result:
			user = result.getInfo()

		return user