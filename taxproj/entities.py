from abc import ABC, abstractmethod

class User(object):

    def __init__(self, user_id, handphone, password, name, created_at, updated_at):
        self._user_id = user_id
        self._handphone = handphone
        self._name  = name
        self._password = password
        self._created_at = created_at
        self._updated_at = updated_at
    
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def handphone(self):
        return self._handphone
    
    @property
    def name(self):
        return self._name

    @property
    def password(self):
        return self._password

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

class TaxObject(ABC):

    def __init__(self, tax_id, name, tax_code, type, price, refundable, created_at, updated_at):
        self._tax_id = tax_id
        self._name = name
        self._tax_code = tax_code
        self._type = type
        self._price = int(price)
        self._refundable = refundable
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def tax_id(self):
        return self._tax_id

    @property
    def name(self):
        return self._name
    
    @property
    def tax_code(self):
        return self._tax_code
    
    @property
    def type(self):
        return self._type

    @property
    def price(self):
        return self._price

    @property
    def refundable(self):
        return self._refundable
    
    @property
    def tax(self):
        return self.calculateTax()

    @property
    def amount(self):
        return self.calculateAmount()

    @property
    def created_at(self):
        return self._created_at
    
    @property
    def updated_at(self):
        return self._updated_at

    @abstractmethod
    def calculateTax(self):
        pass
    
    @abstractmethod
    def calculateAmount(self):
        pass

class Food(TaxObject):

    def __init__(self, tax_id, tax_code, name, price, created_at, updated_at):
        super().__init__(tax_id, name, tax_code, 'food', price, True, created_at, updated_at)

    def calculateTax(self):
        return float((10 / 100) * self._price)
    
    def calculateAmount(self):
        return float(self._price) + self.calculateTax()

class Tobacco(TaxObject):

    def __init__(self, tax_id, tax_code, name, price, created_at, updated_at):
        super().__init__(tax_id, name, tax_code, 'tobacco', price, False, created_at, updated_at)

    def calculateTax(self):
        return float(10 + float((2/ 100) * self._price))
    
    def calculateAmount(self):
        return float(self._price) + self.calculateTax()

class Entertainment(TaxObject):

    def __init__(self, tax_id, tax_code, name, price, created_at, updated_at):
        super().__init__(tax_id, name, tax_code, 'entertainment', price, False, created_at, updated_at)

    def calculateTax(self):
        if(self._price < 100):
            return 0

        return float((1/ 100) * (self._price - 100))
    
    def calculateAmount(self):
        return float(self._price) + self.calculateTax()