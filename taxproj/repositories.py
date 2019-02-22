'''Author: Fadhlan Ridhwanallah
   Date: 22 February 2019'''
   
from .models import ORMUser, ORMTaxObject
from .entities import User
from taxproj import factories

class UserDatabaseRepo(object):

    def insert(self, user_data):
        orm_user = ORMUser.objects.create(user_id=user_data['user_id'], handphone=user_data['handphone'],
                                          password=user_data['password'], name=user_data['name'],
                                          created_at=user_data['created_at'], updated_at=user_data['updated_at'])

        return self._decode_orm_user(orm_user=orm_user)

    def get(self, handphone):
        orm_user = ORMUser.objects.get(handphone=handphone)
       
        return self._decode_orm_user(orm_user=orm_user)

    def _decode_orm_user(self, orm_user):
        return User(user_id=orm_user.user_id, handphone=orm_user.handphone,
                    password=orm_user.password, name=orm_user.name,
                    created_at=orm_user.created_at, updated_at=orm_user.updated_at)

class TaxObjectDatabaseRepo(object):

    def insert(self, tax_data):
        orm_user = ORMUser.objects.get(user_id=tax_data['user_id'])

        orm_tax_object = ORMTaxObject.objects.create(tax_id=tax_data['tax_id'], user_id=orm_user, 
                                                     tax_code=tax_data['tax_code'], name=tax_data['name'],
                                                     price=tax_data['price'], created_at=tax_data['created_at'],
                                                     updated_at=tax_data['updated_at'])
        
        return self._decode_orm_tax_object(orm_tax_object=orm_tax_object)

    def get(self, user_id):
        orm_tax_object = ORMTaxObject.objects.filter(user_id=user_id)

        return self._decode_orm_tax_objects(orm_tax_objects=orm_tax_object)


    def _decode_orm_tax_object(self, orm_tax_object):
        return factories.TaxObjectFactory.new(tax_id=orm_tax_object.tax_id, 
                                              tax_code=orm_tax_object.tax_code,
                                              name=orm_tax_object.name, 
                                              price=orm_tax_object.price, 
                                              created_at=orm_tax_object.created_at, 
                                              updated_at=orm_tax_object.updated_at)
    
    def _decode_orm_tax_objects(self, orm_tax_objects):
        list_orm_tax = []

        for orm_tax_object in orm_tax_objects:
            list_orm_tax.append(self._decode_orm_tax_object(orm_tax_object))
        
        return list_orm_tax