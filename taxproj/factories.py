'''Author: Fadhlan Ridhwanallah
   Date: 22 February 2019'''
   
from .repositories import UserDatabaseRepo, TaxObjectDatabaseRepo
from .unit_repositories import UserRepo, TaxObjectRepo
from .interactors import SignUpUserInteractor, SignInUserInteractor, InsertTaxObjectInteractor, GetTaxObjectInteractor
from .views import UserView, TaxObjectView
from .entities import Food, Tobacco, Entertainment

class UserDatabaseRepoFactory(object):

	@staticmethod
	def get():
		return UserDatabaseRepo()

class UserRepoFactory(object):

	@staticmethod
	def get():
		db_repo = UserDatabaseRepoFactory.get()
		return UserRepo(db_repo)


class UserInteractorFactory(object):

	@staticmethod
	def signup():
		user_repo = UserRepoFactory.get()
		return SignUpUserInteractor(user_repo)

	@staticmethod
	def signin():
		user_repo = UserRepoFactory.get()
		return SignInUserInteractor(user_repo)

class UserViewFactory(object):

	@staticmethod
	def signup():
		user_interactor = UserInteractorFactory.signup()
		return UserView(user_interactor)

	@staticmethod
	def signin():
		user_interactor = UserInteractorFactory.signin()
		return UserView(user_interactor)



class TaxObjectFactory(object):

	@staticmethod
	def new(tax_id, name, price, tax_code, created_at, updated_at):
		if(tax_code == 1):
			return Food(tax_id, tax_code, name, price, created_at, updated_at)
		elif(tax_code == 2):
			return Tobacco(tax_id, tax_code, name, price, created_at, updated_at)
		else:
			return Entertainment(tax_id, tax_code, name, price, created_at, updated_at)

class TaxObjectDatabaseRepoFactory(object):

	@staticmethod
	def get():
		return TaxObjectDatabaseRepo()

class TaxObjectRepoFactory(object):

	@staticmethod
	def get():
		db_repo = TaxObjectDatabaseRepoFactory.get()
		return TaxObjectRepo(db_repo)


class TaxObjectInteractorFactory(object):

	@staticmethod
	def insert():
		tax_object_repo = TaxObjectRepoFactory.get()
		return InsertTaxObjectInteractor(tax_object_repo)
	
	@staticmethod
	def get():
		tax_object_repo = TaxObjectRepoFactory.get()
		return GetTaxObjectInteractor(tax_object_repo)

class TaxObjectViewFactory(object):

	@staticmethod
	def insert():
		tax_object_iterator = TaxObjectInteractorFactory.insert()
		return TaxObjectView(tax_object_iterator)

	@staticmethod
	def get():
		tax_object_iterator = TaxObjectInteractorFactory.get()
		return TaxObjectView(tax_object_iterator)