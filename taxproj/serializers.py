'''Author: Fadhlan Ridhwanallah
   Date: 22 February 2019'''
   
class UserSerializer(object):

    @staticmethod
    def serialize(user):
        return {
            "user_id": user.user_id,
            "name": user.name,
            "handphone": user.handphone
        }

class TaxObjectSerializer(object):

    @staticmethod
    def serialize(tax_object):
        refundable = "Yes"

        if(tax_object.refundable == False):
            refundable = "No"

        return {
            "tax_id": str(tax_object.tax_id),
            "name": tax_object.name,
            "tax_code": int(tax_object.tax_code),
            "type": tax_object.type,
            "refundable": refundable,
            "price": tax_object.price,
            "tax": tax_object.tax,
            "amount": tax_object.amount
        }

    @staticmethod
    def serialize_list(tax_objects):
        price_sub_total = 0
        tax_sub_total = 0
        grand_total = 0
        list_tax_object = []

        for tax_object in tax_objects:
            list_tax_object.append(TaxObjectSerializer.serialize(tax_object))
            price_sub_total += tax_object.price
            tax_sub_total += tax_object.tax
            grand_total += tax_object.amount
        
        return {
            "tax_object": list_tax_object,
            "price_sub_total": price_sub_total,
            "tax_sub_total": tax_sub_total,
            "grand_total": grand_total
        }