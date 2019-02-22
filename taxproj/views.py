import json

from django.http import HttpResponse
from django.views import View
import json
from .serializers import UserSerializer, TaxObjectSerializer

class SignUp(View):

    view_factory = None

    def post(self, request):
        body, status = self.view_factory.signup().signup(body=json.loads(request.body))

        return HttpResponse(json.dumps(body), status=status,
                            content_type='application/json')

class SignIn(View):

    view_factory = None

    def post(self, request):
        body, status = self.view_factory.signin().signin(body=json.loads(request.body))

        return HttpResponse(json.dumps(body), status=status,
                            content_type='application/json')

class InsertTaxObject(View):
    view_factory = None

    def post(self, request, user_id):
        requestBody = json.loads(request.body)
        requestBody['user_id'] = user_id

        body, status = self.view_factory.insert().insert(body=requestBody)

        return HttpResponse(json.dumps(body), status=status,
                            content_type='application/json')

class GetTaxObject(View):
    view_factory = None

    def get(self, request, user_id):
        body, status = self.view_factory.get().get(user_id=user_id)

        return HttpResponse(json.dumps(body), status=status,
                            content_type='application/json')

class UserView(object):

    def __init__(self, user_interactor):
        self.user_interactor = user_interactor

    def signup(self, body):
        try:
            self.user_interactor.set_params(request=body)
            user = self.user_interactor.execute()

        except Exception as exception:
            body = {"message": str(exception)}
            status = 404
        else:
            body = {}
            status = 200

        return body, status

    def signin(self, body):
        try:
            self.user_interactor.set_params(request=body)
            user = self.user_interactor.execute()

        except Exception as exception:
            body = {"message": str(exception)}
            status = 404
        else:
            body = UserSerializer.serialize(user)
            status = 200

        return body, status

class TaxObjectView(object):

    def __init__(self, tax_object_interactor):
        self.tax_object_interactor = tax_object_interactor

    def insert(self, body):
        try:
            self.tax_object_interactor.set_params(request=body)
            tax_object = self.tax_object_interactor.execute()

        except Exception as exception:
            body = {"message": str(exception)}
            status = 404
        else:
            body = TaxObjectSerializer.serialize(tax_object)
            status = 200

        return body, status

    def get(self, user_id):
        try:
            self.tax_object_interactor.set_params(request=user_id)
            tax_object = self.tax_object_interactor.execute()

        except Exception as exception:
            body = {"message": str(exception)}
            status = 404
        else:
            body = TaxObjectSerializer.serialize_list(tax_object)
            status = 200

        return body, status