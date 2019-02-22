'''Author: Fadhlan Ridhwanallah
   Date: 22 February 2019'''
   
from abc import ABC, abstractmethod
from .utils import ParamHelper
from django.utils import timezone
import uuid
import hashlib

class Interactor(ABC):
    @abstractmethod
    def set_params(self, request):
        pass

    @abstractmethod
    def execute(self):
        pass

class SignUpUserInteractor(Interactor):

    def __init__(self, user_repo):
        self._user_repo = user_repo
    
    def set_params(self, request):
        ParamHelper.isBlank(param=request['handphone'], message="Handphone must not blank.")
        ParamHelper.isBlank(param=request['password'], message="Password must not blank.")
        ParamHelper.isBlank(param=request['name'], message="Name must not blank.")

        self._request = request

    def execute(self):
        self._request['user_id'] = uuid.uuid1()
        self._request['password'] = hashlib.sha1(self._request['password'].encode()).hexdigest()
        self._request['created_at'] = timezone.now()
        self._request['updated_at'] = timezone.now()
        
        return self._user_repo.insert(user_data=self._request)

class SignInUserInteractor(Interactor):

    def __init__(self, user_repo):
        self._user_repo = user_repo
    
    def set_params(self, request):
        ParamHelper.isBlank(param=request['handphone'], message="Handphone must not blank.")
        ParamHelper.isBlank(param=request['password'], message="Password must not blank.")

        self._request = request

    def execute(self):
        user = self._user_repo.get(handphone=self._request['handphone'])
        
        assert(user.password == hashlib.sha1(self._request['password'].encode()).hexdigest()), "Password is not valid"
        
        return user

class InsertTaxObjectInteractor(Interactor):
    def __init__(self, tax_repo):
        self._tax_repo = tax_repo
    
    def set_params(self, request):
        ParamHelper.isBlank(param=request['user_id'], message="User ID must not blank.")
        ParamHelper.isBlank(param=request['tax_code'], message="Tax code must not blank.")
        ParamHelper.isBlank(param=request['name'], message="Name must not blank.")
        ParamHelper.isBlank(param=request['price'], message="Price must not blank.")

        self._request = request

    def execute(self):
        self._request['tax_id'] = uuid.uuid1()
        self._request['created_at'] = timezone.now()
        self._request['updated_at'] = timezone.now()
        
        return self._tax_repo.insert(tax_data=self._request)

class GetTaxObjectInteractor(Interactor):
    def __init__(self, tax_repo):
        self._tax_repo = tax_repo
    
    def set_params(self, request):
        ParamHelper.isBlank(param=request, message="User ID must not blank.")

        self._request = request

    def execute(self):
        return self._tax_repo.get(user_id=self._request)