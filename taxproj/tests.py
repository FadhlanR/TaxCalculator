from django.test import TestCase
from .models import ORMUser, ORMTaxObject
from .factories import TaxObjectFactory 
import uuid
import hashlib
from django.utils import timezone

class TaxObjectTestCase(TestCase):
    def setUp(self):
        password = "password"
        self.orm_user = ORMUser.objects.create(user_id=uuid.uuid1(), password=hashlib.sha1(password.encode()).hexdigest(),
                                          name="Fadhlan Ridhwanallah", handphone="085749216686", created_at=timezone.now(),
                                          updated_at=timezone.now())

    def test_food_tax_object(self):
        orm_tax_object = ORMTaxObject.objects.create(tax_id=uuid.uuid1(), user_id=self.orm_user, 
                                    tax_code=1, name='Big Mac',
                                    price=1000, created_at=timezone.now(),
                                    updated_at=timezone.now())
        
        tax_object = TaxObjectFactory.new(tax_id=orm_tax_object.tax_id, 
                                         tax_code=orm_tax_object.tax_code,
                                         name=orm_tax_object.name, 
                                         price=orm_tax_object.price, 
                                         created_at=orm_tax_object.created_at, 
                                         updated_at=orm_tax_object.updated_at)
        
        assert(tax_object.refundable == True), "Refundable is wrong"
        assert(tax_object.tax == 100), "Tax calculation is failed"
        assert(tax_object.amount == 1100), "Amount calculation is failed"

    def test_tobacco_tax_object(self):
        orm_tax_object = ORMTaxObject.objects.create(tax_id=uuid.uuid1(), user_id=self.orm_user, 
                                    tax_code=2, name='Djarum',
                                    price=1000, created_at=timezone.now(),
                                    updated_at=timezone.now())

        tax_object = TaxObjectFactory.new(tax_id=orm_tax_object.tax_id, 
                                         tax_code=orm_tax_object.tax_code,
                                         name=orm_tax_object.name, 
                                         price=orm_tax_object.price, 
                                         created_at=orm_tax_object.created_at, 
                                         updated_at=orm_tax_object.updated_at)
        
        assert(tax_object.refundable == False), "Refundable is wrong"
        assert(tax_object.tax == 30), "Tax calculation is failed"
        assert(tax_object.amount == 1030), "Amount calculation is failed"

    def test_entertainment_tax_object(self):
        orm_tax_object = ORMTaxObject.objects.create(tax_id=uuid.uuid1(), user_id=self.orm_user, 
                                    tax_code=3, name='Movie',
                                    price=150, created_at=timezone.now(),
                                    updated_at=timezone.now())

        tax_object = TaxObjectFactory.new(tax_id=orm_tax_object.tax_id, 
                                         tax_code=orm_tax_object.tax_code,
                                         name=orm_tax_object.name, 
                                         price=orm_tax_object.price, 
                                         created_at=orm_tax_object.created_at, 
                                         updated_at=orm_tax_object.updated_at)
        
        assert(tax_object.refundable == False), "Refundable is wrong"
        assert(tax_object.tax == 0.5), "Tax calculation is failed"
        assert(tax_object.amount == 150.5), "Amount calculation is failed"