'''Author: Fadhlan Ridhwanallah
   Date: 22 February 2019'''
   
class UserRepo(object):

    def __init__(self, db_repo):
        self.db_repo = db_repo

    def insert(self, user_data):
        user = self.db_repo.insert(user_data)
        
        return user
    
    def get(self, handphone):
        user = self.db_repo.get(handphone)
        return user

class TaxObjectRepo(object):

    def __init__(self, db_repo):
        self.db_repo = db_repo

    def insert(self, tax_data):
        tax_object = self.db_repo.insert(tax_data)
    
        return tax_object

    def get(self, user_id):
        tax_object = self.db_repo.get(user_id)
        return tax_object